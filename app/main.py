from fastapi import FastAPI
from app.routes import logs, status, version, resources
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:3000",  # React app
]
app.include_router(status.router)
app.include_router(logs.router)
app.include_router(version.router)
app.include_router(resources.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)