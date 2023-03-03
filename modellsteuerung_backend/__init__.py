import subprocess
import time

from fastapi import FastAPI

from .logger import get_logger
from .swarm import backend

app = FastAPI()
logger = get_logger(__name__)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")
    backend.start()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
    backend.teardown_requested = True
    backend.join()
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
