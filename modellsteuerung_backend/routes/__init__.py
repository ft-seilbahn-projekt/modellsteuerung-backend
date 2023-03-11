from fastapi import FastAPI


def setup_routes(app: FastAPI):
    from . import notifications
    app.include_router(notifications.router)

    from . import drivectl
    app.include_router(drivectl.router)

    from . import desk
    app.include_router(desk.router)
