from llm_proxy.models import LLMResponse
from llm_proxy.retry import retry


class AllProvidersFailed(Exception):
    pass


def call_with_fallback(
    providers,
    prompt: str,
    max_attempt: int = 2,
    base_delay: float = 1.0,
) -> LLMResponse:
    if not providers:
        raise ValueError("providers list is empty")

    failures = []

    for provider in providers:
        name = type(provider).__name__
        try:
            return retry(
                lambda: provider.call(prompt),
                max_attempt=max_attempt,
                base_delay=base_delay,
            )
        except Exception as error:
            failures.append(f"{name}: {error}")

    raise AllProvidersFailed("All providers failed. " + " | ".join(failures))


if __name__ == "__main__":

    class FailingProvider:
        def __init__(self):
            self.calls = 0

        def call(self, prompt):
            self.calls += 1
            raise ConnectionError("down")

    class WorkingProvider:
        def __init__(self):
            self.calls = 0

        def call(self, prompt):
            self.calls += 1
            return LLMResponse(
                text="ok",
                provider="Working",
                model="fake",
                input_tokens=1,
                output_tokens=1,
                latency_ms=0.0,
                cost=0.0,
            )

    failing = FailingProvider()
    working = WorkingProvider()
    result = call_with_fallback([failing, working], "hi", base_delay=0.01)
    print("test 1:", result.provider, "| failing tried", failing.calls, "times")

    failing = FailingProvider()
    working = WorkingProvider()
    result = call_with_fallback([working, failing], "hi", base_delay=0.01)
    print("test 2:", result.provider, "| failing tried", failing.calls, "times")

    try:
        call_with_fallback(
            [FailingProvider(), FailingProvider()], "hi", base_delay=0.01
        )
    except AllProvidersFailed as error:
        print("test 3:", error)

    try:
        call_with_fallback([], "hi")
    except ValueError as error:
        print("test 4:", error)