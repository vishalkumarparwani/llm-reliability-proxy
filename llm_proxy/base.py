from abc import ABC, abstractmethod

from llm_proxy.models import LLMResponse


class BaseProvider(ABC):

    @abstractmethod
    def call(self, prompt: str) -> LLMResponse:
        pass