import os
import time

import httpx
from dotenv import load_dotenv

from llm_proxy.base import BaseProvider
from llm_proxy.models import LLMResponse

load_dotenv()


class OllamaProvider(BaseProvider):

    def __init__(self):
        self.host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        self.model = os.getenv("OLLAMA_MODEL", "qwen3:8b")

    def call(self, prompt: str) -> LLMResponse:
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            "stream": False,
        }

        start = time.perf_counter()

        response = httpx.post(
            f"{self.host}/api/chat",
            json=payload,
            timeout=300,
        )
        response.raise_for_status()

        latency_ms = (time.perf_counter() - start) * 1000

        data = response.json()

        return LLMResponse(
            text=data["message"]["content"],
            provider="Ollama",
            model=self.model,
            input_tokens=data.get("prompt_eval_count") or 0,
            output_tokens=data.get("eval_count") or 0,
            latency_ms=latency_ms,
            cost=0.0,
        )


if __name__ == "__main__":
    provider = OllamaProvider()
    result = provider.call("what's 2+2")
    print(result)