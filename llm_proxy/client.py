from llm_proxy.models import LLMResponse
from llm_proxy.retry import retry


def get_provider(name: str):
    pass


class LLMClient:

    def __init__(self, provider_name: str):
        pass

    def call(self, prompt: str) -> LLMResponse:
        pass