import json
import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.utils.config import SHARED_DATA_PATH

app = FastAPI(
    title="Compliance Checker API",
    description="Single-agent compliance pipeline for RBI/SEBI/MCA circulars",
    version="1.0.0",
)

# ── CORS ───────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Helpers ────────────────────────────────────────────────────────────────

def shared_path(filename: str) -> Path:
    return Path(SHARED_DATA_PATH) / filename


def read_json(filename: str):
    path = shared_path(filename)
    if not path.exists() or path.stat().st_size == 0:
        return None
    with open(path, "r") as f:
        return json.load(f)


def write_json(filename: str, data: dict):
    path = shared_path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


# ── Endpoints ──────────────────────────────────────────────────────────────

@app.post("/run_compliance_crew")
async def run_compliance_crew():
    """
    Triggers the ComplianceOrchestratorAgent pipeline.
    Phase 1: Returns a mock success response.
    Phase 2: This will call crew.py and write all shared_data/ JSON files.
    """
    # ── MOCK RESPONSE (Phase 1) ──
    # TODO (Phase 2 — AI Dev): Replace this block with:
    #   from backend.crew import ComplianceOrchestratorAgent
    #   agent = ComplianceOrchestratorAgent()
    #   result = agent.run()
    # Then write result to shared_data/ JSON files.

    mock_result = {
        "status": "complete",
        "message": "Mock run complete — wire to crew.py in Phase 2",
        "run_id": "run_mock",
    }

    write_json("simulation_results.json", {
        "run_id": "run_mock",
        "status": "complete",
        "steps_completed": ["scrape", "diff", "rag_map", "amend", "report", "evolve"],
        "duration_seconds": 0,
    })

    return mock_result


@app.get("/status")
async def get_status():
    """
    Returns the current run status from simulation_results.json.
    Frontend polls this every 3 seconds during the live-agents screen.
    """
    data = read_json("simulation_results.json")
    if data is None:
        return {"status": "not_started"}
    return data


@app.get("/report")
async def get_report():
    """
    Returns the latest compliance report from latest_report.json.
    """
    data = read_json("latest_report.json")
    if data is None:
        return {"message": "No report available yet. Run a compliance check first."}
    return data


@app.get("/evolution")
async def get_evolution():
    """
    Returns the evolution history from evolution_history.json.
    """
    data = read_json("evolution_history.json")
    if data is None:
        return {"runs": []}
    return data


@app.post("/reset")
async def reset():
    """
    Phase 5 — Resets demo state.
    Clears shared_data/ JSON files.
    PDF restore from backup is handled by AI Dev in crew.py.
    """
    write_json("latest_report.json", {})
    write_json("evolution_history.json", {"runs": []})
    write_json("simulation_results.json", {"status": "not_started"})

    return {"status": "reset", "message": "shared_data/ cleared. Ready for a fresh demo run."}


@app.get("/health")
async def health():
    return {"status": "ok", "service": "compliance-checker-api"}
