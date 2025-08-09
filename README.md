# Apex Operator (Open Source)

This repository contains the skeleton for the **Apex Operator** — an open‑source swarm of AI agents designed to automate ethical, compliant, revenue‑driven tasks across multiple verticals.

## Structure

```
text
apex-oss/
├── apps/
│   ├── backend/        # FastAPI backend and LangGraph agent orchestrator
│   └── frontend/       # Next.js frontend dashboard (placeholder)
├── agents/             # Individual AI agents (niche hunter, offer smith, etc.)
├── integrations/       # Connectors for CRM, mail, vector stores and search
├── infra/              # Infrastructure configuration (Docker Compose, Traefik)
├── n8n/                # n8n workflow exports for outreach and automation
└── ops/                # Operational docs and environment configuration
```

## Getting Started

1. Copy `.env.example` to `.env` and fill in your environment variables.
2. Run `make up` to build and start the stack via Docker Compose.
3. Access the dashboard at `http://localhost:3000` and the API at `http://localhost:8000`.

This project is a work in progress. It is intended as a foundation for building a fully autonomous agent swarm using entirely open‑source technologies. Contributions and improvements are welcome!
