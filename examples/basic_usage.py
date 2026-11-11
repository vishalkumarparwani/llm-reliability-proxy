from llm_proxy import LLMClient

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