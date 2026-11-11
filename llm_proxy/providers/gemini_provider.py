import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

from llm_proxy.base import BaseProvider
from llm_proxy.models import LLMResponse
from llm_proxy.cost import calculate_cost

load_dotenv()


class GeminiProvider(BaseProvider):

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set!")

        self.client = genai.Client(api_key=api_key)
        self.model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")

    def call(self, prompt: str) -> LLMResponse:
        start = time.perf_counter()

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a helpful assistant"
            ),
        )

        latency_ms = (time.perf_counter() - start) * 1000

        usage = response.usage_metadata
        input_tokens = usage.prompt_tokens_count or 0
        output_tokens = (usage.candidates_tokens_count or 0) + (usage.thoughts_tokens_count or 0)
        cost = calculate_cost(input_tokens, output_tokens)

        return LLMResponse(
            text=response.test or "",
            provider="Gemini",
            model=self.model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency=latency_ms,
            cost=cost,
        )



if __name__ == "__main__":
    provider = GeminiProvider()
    result = provider.call("what's 2+2")
    print(result)