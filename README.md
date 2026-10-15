# LLM Reliability & Cost Proxy

A provider-agnostic Python middleware SDK for improving the reliability and cost visibility of Large Language Model (LLM) API calls through a unified interface.

**Internship Capstone Project - FlyRank AI | Backend AI Developer Track**

## Overview

LLM providers expose different APIs, response formats, rate limits, and pricing models. This project aims to provide a consistent interface for interacting with multiple providers while adding reliability and cost-management capabilities.

## Features

### Implemented
- **Provider abstraction:** A common `BaseProvider` interface.
- **Unified response model:** An `LLMResponse` data structure.

### Planned
- **Provider adapters:** Anthropic Claude, Groq, Google Gemini, and Ollama.
- **Response caching:** Avoid redundant API calls where appropriate.
- **Retry mechanism:** Handle transient failures with configurable backoff.
- **Automatic fallback:** Switch providers when the primary provider fails.
- **Rate limiting:** Control request frequency.
- **Cost tracking:** Estimate and record per-call token usage and cost.

## Supported Providers

| Provider | Status |
|---|---|
| Anthropic Claude | Planned |
| Groq | Planned |
| Google Gemini | Planned |
| Ollama (local models) | Planned |

## Architecture

The intended architecture separates provider-specific implementations from the reliability middleware.

```text
Application
    |
    v
LLM Reliability Proxy
    |
    +-- Caching
    +-- Retry & Fallback
    +-- Rate Limiting
    +-- Cost Tracking
    |
    v
BaseProvider Interface
    |
    +-- Anthropic Adapter
    +-- Groq Adapter
    +-- Gemini Adapter
    +-- Ollama Adapter
    |
    v
LLM Providers
```

*Architecture represents the planned design; components are not necessarily implemented yet.*

## Tech Stack

- Python
- Object-oriented design and abstract interfaces
- Provider SDKs and HTTP APIs
- Pytest (planned for testing)

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd LLM_reliability_proxy
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Add the required provider API keys to a local `.env` file as provider integrations are implemented. Never commit API keys or other secrets.

## Project Goals

- Provide a consistent interface across multiple LLM providers.
- Improve resilience to transient errors and provider outages.
- Reduce unnecessary API calls through caching.
- Track token usage and estimated inference costs.
- Support local models alongside hosted providers.

## Project Status

**Work in Progress.** The provider abstraction and unified response model are implemented. Additional integrations and reliability features are planned.

## Acknowledgment

Developed as the capstone project for the **FlyRank AI Backend AI Developer Internship**.
