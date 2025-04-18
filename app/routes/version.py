from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/version")
def get_version():
    url = "https://api.github.com/repos/DSC-McMaster-U/mac-FAQ-chatbot"
    response = requests.get(url)
    print(response.json())
    if response.status_code ==200:
        data = response.json()
        return {
            "repo": data["full_name"],
            "default_branch": data["default_branch"],
            "last_updated": data["updated_at"]
        }
    return {"error": "Could not fetch repo data"}