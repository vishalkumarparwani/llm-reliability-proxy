from llm_proxy.models import LLMResponse
from llm_proxy.retry import retry

PROVIDER_NAMES = ["anthropic", "openai", "gemini", "groq", "ollama"]


def get_provider(name: str):
    if name == "anthropic":
        from llm_proxy.providers.anthropic_provider import AnthropicProvider
        return AnthropicProvider()
    elif name == "openai":
        from llm_proxy.providers.openai_provider import OpenAIProvider
        return OpenAIProvider()
    elif name == "gemini":
        from llm_proxy.providers.gemini_provider import GeminiProvider
        return GeminiProvider()
    elif name == "groq":
        from llm_proxy.providers.groq_provider import GroqProvider
        return GroqProvider()
    elif name == "ollama":
        from llm_proxy.providers.ollama_provider import OllamaProvider
        return OllamaProvider()
    else:
        raise ValueError(
            f"Unknown provider '{name}'. Valid providers: {', '.join(PROVIDER_NAMES)}"
        )


class LLMClient:

    def __init__(self, provider_name: str):
        self.provider = get_provider(provider_name)

    def call(self, prompt: str) -> LLMResponse:
        return retry(lambda: self.provider.call(prompt))


if __name__ == "__main__":
    try:
        LLMClient("nope")
    except ValueError as error:
        print("unknown provider error:", error)

    client = LLMClient("groq")
    result = client.call("what's 2+2")
    print(result)