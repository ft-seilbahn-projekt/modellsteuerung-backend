import dotenv
from starlette.middleware.cors import CORSMiddleware

from .state import poti_state

dotenv.load_dotenv()

import subprocess
import time

from fastapi import FastAPI

from .logger import get_logger
from .swarm import backend

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = get_logger(__name__)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")
    backend.start()
    logger.info("Startup complete")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
    backend.teardown_requested = True
    logger.info("Shutdown complete")


@app.get("/")
def read_root():
    git_commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()

    return {
        "project": "modellsteuerung_backend",
        "version": "0.0.1",
        "description": "Backend for the ft-seilbahn-project",
        "author": "ft-seilbahn-project",
        "contact": "christian.bergschneider@gmx.de",
        "license": "MIT",
        "time": time.time(),
        "commit": git_commit,
        "docs": [
            "/docs",
            "/redoc",
        ],
    }


@app.get("/poti")
def read_poti():
    return {
        "poti": poti_state()
    }
