from fastapi import APIRouter

from modellsteuerung_backend.state.notifications import notifications, Notification

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"]
)


@router.get("/")
async def get_notifications() -> list[Notification]:
    return notifications.get_notifications()


@router.post("/")
async def add_notification(notification: Notification) -> Notification:
    notifications.add_notification(notification)
    return notification


@router.put("/")
async def update_notification(notification: Notification):
    notifications.remove_notification_by_id(notification.id)
    notifications.add_notification(notification)


@router.delete("/{identifier}")
async def remove_notification(identifier: int):
    notifications.remove_notification_by_id(identifier)
