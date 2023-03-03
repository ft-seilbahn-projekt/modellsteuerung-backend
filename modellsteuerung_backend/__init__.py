import subprocess

from fastapi import FastAPI

import time

app = FastAPI()


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
