"""Synthetic scheduler: no network, process launch, or real job."""
import json

print(json.dumps({
    "job_id": "job-041",
    "status": "RUNNING",
    "checked_at": "2026-10-16T00:00:00Z",
    "completed_shards": [0, 1, 2],
    "remaining_shards": [3],
    "run_id": "study-012",
}))
