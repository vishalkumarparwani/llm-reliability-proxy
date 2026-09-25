import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=GROQ_API_KEY)


def temporary_chat(messages):
    groq_messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        }
    ]

    for message in messages:
        groq_messages.append(
            {
                "role": message["role"],
                "content": message["content"]
            }
        )

    return client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=groq_messages,
        temperature=0.3
    )


messages = [
    {"role": "user", "content": "Write a Groq query to find all documents where the 'status' field is 'active'."}
]

response = temporary_chat(messages)

print(f"Response: {response.choices[0].message.content}")
print(f"Usage: {response.usage}")