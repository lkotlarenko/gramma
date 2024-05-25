from plyer import notification
from src.config import APP_NAME, APP_ICON


def notify(title: str, message: str, timeout: int) -> None:
    notification.notify(
        title=title,
        message=message,
        app_name=APP_NAME,
        app_icon=APP_ICON,
        timeout=timeout,
    )
