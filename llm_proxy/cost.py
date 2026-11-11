from llm_proxy.config import PRICING

def calculate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    if model not in PRICING:
        raise ValueError(f"Pricing information for model '{model}' not found")

    pricing_info = PRICING[model]
    input_cost = (input_tokens / 1000000) * pricing_info["input_per_million"]
    output_cost = (output_tokens / 1000000) * pricing_info["output_per_million"]

    return input_cost + output_cost




if __name__ == "__main__":
    print(calculate_cost("openai/gpt-oss-120b", 86, 33))
    try:
        calculate_cost("fake-model", 86, 33)
    except ValueError as error:
        print("unknown model:", error)