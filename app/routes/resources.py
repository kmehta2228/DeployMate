from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/resources")
def get_resource_usage():
    return {
        "cpu_usage_percent": round(random.uniform(20, 75), 2),
        "memory_usage_gb": round(random.uniform(2.0, 6.5), 2),
        "storage_remaining_gb": round(random.uniform(50.0, 200.0), 2)
    }
