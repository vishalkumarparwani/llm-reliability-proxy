import os
import time

from dotenv import load_dotenv
from anthropic import Anthropic

from .base import BaseProvider
from .models import LLMResponse

load_dotenv()

class ClaudeProvider(BaseProvider):

    def __init__(self):
        api_key = os.getenv("CLAUDE_API_KEY")

        if not api_key:
            raise ValueError("CLAUDE_API_KEY environment variable is not set!")

        self.client = Anthropic(api_key=api_key)
        self.model = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-5")
        

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

        return LLMResponse(
            text=response.content[0].text,
            provider="Claude",
            model=self.model,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            latency_ms=latency_ms,
            cost=0.0,
        )


if __name__ == "__main__":
    provider = ClaudeProvider()
    result = provider.call("what's 2+2")
    print(result)