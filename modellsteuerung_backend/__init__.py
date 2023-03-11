from dataclasses import dataclass

import dotenv

# This a dependency of fastapi and is installed by pip
# noinspection PyPackageRequirements
from starlette.middleware.cors import CORSMiddleware

from .routes import setup_routes

dotenv.load_dotenv()

import subprocess
import time

from fastapi import FastAPI

from .logger import get_logger
from .hardware import backend

app = FastAPI(
    title="Modellsteuerung Backend",
    description="Backend for the ft.seilbahn-projekt",
    version="0.0.1"
)

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


@dataclass
class Info:
    project: str
    version: str
    description: str
    author: str
    contact: str
    license: str
    time: float
    commit: str
    docs: list[str]


@app.get("/", summary="Get information about the backend")
def read_root() -> Info:
    git_commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()

    return Info(
        project="modellsteuerung_backend",
        version="0.0.1",
        description="Backend for the ft-seilbahn-project",
        author="ft-seilbahn-project",
        contact="christian.bergschneider@gmx.de",
        license="MIT",
        time=time.time(),
        commit=git_commit,
        docs=[
            "/docs",
            "/redoc",
        ],
    )


setup_routes(app)
