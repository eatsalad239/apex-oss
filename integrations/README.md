# Integrations

This directory contains connectors and integration modules for various third‑party services used by the Apex Operator platform.

## Structure

Each integration is placed in its own subdirectory. The following are typical categories:

- **crm/**: Connectors for open‑source CRMs such as SuiteCRM or ERPNext. They handle lead syncing, contact creation, and campaign updates.
- **mail/**: Modules for sending email via SMTP or other mail services. Includes n8n workflows.
- **vector/**: Client wrappers for vector databases like Qdrant or Chroma.
- **search/**: Interfaces to full‑text search engines such as MeiliSearch.

You can add additional integrations as needed. Each submodule should expose a clear API for the agents to use.
