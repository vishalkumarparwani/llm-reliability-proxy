from abc import ABC, abstractmethod
from .models import LLMResponse

class BaseProvider(ABC):
    
    
    @abstractmethod
    def call(self, prompt: str) -> LLMResponse:
        pass

