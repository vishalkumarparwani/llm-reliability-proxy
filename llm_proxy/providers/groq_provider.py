import os
import time

from dotenv import load_dotenv
from groq import Groq

from llm_proxy.base import BaseProvider
from llm_proxy.models import LLMResponse
from llm_proxy.cost import calculate_cost

load_dotenv()

class GroqProvider(BaseProvider):

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set!")

        self.client = Groq(api_key=api_key)
        self.model = "openai/gpt-oss-120b"
        

    def call(self, prompt: str) -> LLMResponse:
        messages = [
            {"role": "system", "content": "You are a helpful bot."},
            {"role": "user", "content": prompt}
        ]

        start = time.perf_counter()

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )

        latency_ms = (time.perf_counter() - start) * 1000

        input_tokens=response.usage.prompt_tokens
        output_tokens=response.usage.completion_tokens

        return LLMResponse(
            text=response.choices[0].message.content,
            provider="Groq",
            model=self.model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,    
            latency_ms=latency_ms,
            cost=calculate_cost(self.model, input_tokens, output_tokens),
        )


if __name__ == "__main__":
    provider = GroqProvider()
    result = provider.call("what's 2+2")
    print(result)