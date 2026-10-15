from dataclasses import dataclass
@dataclass
class LLMResponse:
    text: str
    provider: str
    model: str
    input_tokens: int
    output_tokens: int
    latency_ms: float
    cost: float = 0.0
    cached: bool = False
