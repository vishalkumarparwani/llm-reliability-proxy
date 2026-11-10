import os
import time

from dotenv import load_dotenv
from groq import Groq

from .base import BaseProvider
from .models import LLMResponse

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
        # This measures end-to-end client-observed latency
        latency_ms = (time.perf_counter - start) * 1000

        return LLMResponse(
            text=response.choices[0].message.content,
            provider="Groq",
            model=self.model,
            input_tokens=response.usage.prompt_tokens,
            output_tokens=response.usage.completion_tokens,
            latency_ms=latency_ms,
            cost=0.0,
        )


if __name__ == "__main__":
    provider = GroqProvider()
    result = provider.call("what's 2+2")
    print(result)