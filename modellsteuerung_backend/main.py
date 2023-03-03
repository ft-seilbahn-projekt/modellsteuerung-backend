import uvicorn


def start():
    uvicorn.run("modellsteuerung_backend:app", host="127.0.0.1", port=8000, reload=True)
