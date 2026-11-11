from llm_proxy.fallback import call_with_fallback
from llm_proxy.models import LLMResponse

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

    def __init__(self, providers, max_attempt: int = 2, base_delay: float = 1.0):
        if isinstance(providers, str):
            providers = [providers]

        self.providers = [get_provider(name) for name in providers]
        self.max_attempt = max_attempt
        self.base_delay = base_delay

    def call(self, prompt: str) -> LLMResponse:
        return call_with_fallback(
            self.providers,
            prompt,
            max_attempt=self.max_attempt,
            base_delay=self.base_delay,
        )


if __name__ == "__main__":
    try:
        LLMClient("nope")
    except ValueError as error:
        print("unknown provider:", error)

    single = LLMClient("groq")
    print("single:", single.call("what's 2+2").provider)

    chain = LLMClient(["gemini", "groq"], base_delay=0.1)
    result = chain.call("what's 2+2")
    print("fallback answered by:", result.provider)