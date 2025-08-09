import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
try:
    # Attempt to load variables from a .env file if python-dotenv is available.
    from dotenv import load_dotenv  # type: ignore

    load_dotenv()
except Exception:
    # If python-dotenv isn't installed, just proceed. Environment variables
    # can still be supplied via the system or Docker.
    pass

app = FastAPI(title="Apex Operator Backend")


class CampaignRequest(BaseModel):
    market: str
    vertical: str
    languages: list[str]
    cap_per_day: int | None = None


@app.get("/")
async def root():
    """Simple welcome endpoint"""
    return {"message": "Welcome to the Apex Operator backend!"}


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "ok"}


@app.post("/run-campaign")
async def run_campaign(req: CampaignRequest):
    """
    Placeholder endpoint to kick off a campaign. In a real implementation this
    would dispatch tasks to agents via a job queue or workflow engine.
    """
    # Validate languages list
    if not req.languages:
        raise HTTPException(status_code=400, detail="Languages list cannot be empty")
    # This is just a stub; normally you'd interact with the agent orchestrator here.
    return {
        "message": f"Campaign launched for {req.vertical} in {req.market} with languages {req.languages} and cap {req.cap_per_day}",
        "status": "started",
    }
