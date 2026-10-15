from groq_provider import GroqProvider


provider = GroqProvider()
result = provider.call("what's 2+2")
print(result)