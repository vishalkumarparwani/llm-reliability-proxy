from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class LLMResponse:
    text: str
    input_tokens: int
    output_tokens: int
    provider: str
    cost: float


class BaseProvider(ABC):
    @abstractmethod
    def call(self, prompt: str) -> LLMResponse:
        pass