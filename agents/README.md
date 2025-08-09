# Agents

This directory contains the code for individual AI agents that form the Apex Operator swarm. Each agent is responsible for a specific function and can operate independently or coordinate via the LangGraph orchestrator.

## Modules

- **niche_hunter/** – Identifies underserved niches and market gaps using search trends and public data.
- **offer_smith/** – Crafts compelling offers and pricing strategies tailored to each niche.
- **lead_harvester/** – Collects and enriches lead data from compliant sources.
- **content_engine/** – Generates marketing content such as emails, ads, and landing pages.
- **outreach_ops/** – Builds and executes outbound outreach sequences via email, SMS, or social.
- **closer/** – Assists in closing deals with scripts and objection handling.
- **success_retention/** – Manages customer success and retention workflows.
- **compliance_guard/** – Ensures all activities adhere to legal and ethical standards.
- **ops_optimizer/** – Monitors performance metrics and optimizes agent behavior over time.

You can add additional agents to this directory as needed. Each agent should expose a clear API so that the orchestration layer can invoke it.
