# LLM Reliability & Cost Proxy

A provider-agnostic middleware SDK that wraps LLM API calls with caching, retries, fallback, rate limiting, and per-call cost tracking — behind one consistent interface across multiple providers.

## Status: Work in Progress

Currently implemented:
- Base provider interface (`BaseProvider`, `LLMResponse`)

Planned:
- Provider adapters: Claude, Groq, Gemini, Ollama (local)
- Caching layer
- Retry with backoff
- Automatic fallback between providers
- Rate limiting
- Per-call cost tracking

## Why

Every LLM provider has a different SDK, different response shape, and different pricing model. This project gives one consistent interface (`LLMResponse`) so the rest of an application never needs to know which provider it's actually talking to — including a local model with zero cost and no external rate limit.

## Supported providers (planned)

- Anthropic Claude
- Groq
- Google Gemini
- Ollama (local, e.g. Qwen3 8B)

## Setup

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows
pip install -r requirements.txt
```

## Architecture
