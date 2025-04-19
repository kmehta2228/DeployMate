from fastapi import FastAPI
from app.routes import logs, status, version, resources

app = FastAPI()

app.include_router(status.router)
app.include_router(logs.router)
app.include_router(version.router)
app.include_router(resources.router)