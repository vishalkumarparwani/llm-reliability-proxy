# LLM Reliability Proxy

A Python SDK that wraps LLM API calls behind one interface, with retry, provider fallback, and per call cost tracking.

## Status: work in progress

Working now:

- One provider interface and one response shape across Groq, Anthropic, Gemini, OpenAI and Ollama
- Per call cost from pinned pricing constants, with reasoning tokens counted as output
- Retry with exponential backoff
- Fallback across a list of providers, with a combined failure report

Not built yet:

- Caching, rate limiting, usage log, demo API

## Verification

- Groq: verified with live calls
- Ollama: verified locally
- Anthropic, Gemini, OpenAI: implemented against the official SDKs but not verified live, because their APIs need paid credits or billing that this project avoids

## Install

```
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -e ".[groq]"
```

Copy `.env.example` to `.env` and fill in the keys you use.

## Usage

```python
from llm_proxy import LLMClient

client = LLMClient(["gemini", "groq"])
response = client.call("what's 2+2")
print(response.text, response.provider, response.cost)
```

## Known limitations

- Retry and fallback trigger on any error, not only temporary ones
- Cost uses floats, which is fine for single calls but should be rounded or stored as integers when summing many
- Pricing is pinned by hand and must be updated when providers change prices

## Future ideas

- Semantic caching
- Pricing drift checker\
