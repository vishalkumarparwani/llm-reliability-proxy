import os
import time

from dotenv import load_dotenv
from anthropic import Anthropic

from llm_proxy.base import BaseProvider
from llm_proxy.models import LLMResponse
from llm_proxy.cost import calculate_cost

load_dotenv()

class AnthropicProvider(BaseProvider):

    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is not set!")

        self.client = Anthropic(api_key=api_key)
        self.model = os.getenv("CLAUDE_MODEL", "claude-haiku-5-5")

    def call(self, prompt: str) -> LLMResponse:
        messages = [
            {"role": "user", "content": prompt}
        ]

        start = time.perf_counter()

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system="You are a helpful assistant",
            messages=messages,
        )
        latency_ms = (time.perf_counter() - start) * 1000

        input_tokens=response.usage.input_tokens
        output_tokens=response.usage.output_tokens

        return LLMResponse(
            text=response.content[0].text,
            provider="Anthropic",
            model=self.model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,    
            latency_ms=latency_ms,
            cost=calculate_cost(self.model, input_tokens, output_tokens),
        )


if __name__ == "__main__":
    provider = AnthropicProvider()
    result = provider.call("what's 2+2")
    print(result)