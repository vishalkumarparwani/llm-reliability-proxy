import os
from dotenv import load_dotenv
from groq import Groq
from base import BaseProvider, LLMResponse

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

class GroqProvider(BaseProvider):
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def call(self, prompt: str) -> LLMResponse:
        response = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant bot"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        print(response.usage)
        
        return LLMResponse(
            text = response.choices[0].message.content,
            input_tokens = response.usage.prompt_tokens,
            output_tokens = response.usage.completion_tokens,
            provider = "Groq",
            cost = 0.0,
        )

# if __name__ == "__main__":
    # provider = GroqProvider()
    # result = provider.call("what's 2+2")
    # print(result)