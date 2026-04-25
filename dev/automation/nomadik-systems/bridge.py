cat <<EOF > ~/dev/automation/nomadik-systems/core/bridge.py
from fastapi import FastAPI, BackgroundTasks
from permit_hunter import run_harvest
from core.engine import run_scraper
import uuid

app = FastAPI()

# In-memory store for job status
jobs = {}

@app.get("/")
async def root():
    return {
        "status": "online",
        "system": "Nomadik-C2",
        "capabilities": ["PermitHunter", "Lead-Shield"],
        "location": "Denver-Local"
    }

def execute_task(job_id, trade, params):
    try:
        # This calls your recovered Botasaurus logic
        result = run_harvest({"trade": trade, **params})
        jobs[job_id] = {"status": "completed", "result": result}
    except Exception as e:
        jobs[job_id] = {"status": "failed", "error": str(e)}

@app.post("/harvest/{trade}")
async def start_harvest(trade: str, background_tasks: BackgroundTasks, params: dict = {}):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "running", "trade": trade}
    
    background_tasks.add_task(execute_task, job_id, trade, params)
    
    return {
        "job_id": job_id,
        "message": f"Harvest initiated for {trade}",
        "check_status": f"/status/{job_id}"
    }

@app.get("/status/{job_id}")
async def get_status(job_id: str):
    return jobs.get(job_id, {"status": "not_found"})
EOF
