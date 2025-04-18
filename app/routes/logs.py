from fastapi import APIRouter
router = APIRouter()
@router.get("/logs")
def get_logs():
    return {
        "logs":[
            "Deploy v1.2.3 - Success",
            "Build triggered on main branch",
            "Tests passed(21/21)"
        ]
    }