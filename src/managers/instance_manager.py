import os
import sys

if sys.platform.startswith("win"):
    import win32event
    import win32api
    import winerror
else:
    try:
        import fcntl
    except ImportError:
        fcntl = None

from typing import Optional

from src.utils import notify
from src.config import APP_NAME, NOTIFICATION_TIMEOUT_LONG


class InstanceManager:
    def __init__(self):
        self.mutex: Optional[win32event.PyHandle] = None
        self.lock_fd: Optional[int] = None
        self.ensure_single_instance()

    def ensure_single_instance(self) -> None:
        if sys.platform.startswith("win"):
            self.handle_mutex()
        else:
            if fcntl is not None:
                self.handle_lock_file()
            else:
                notify(
                    "Warning",
                    "Single instance check not supported on this platform.",
                    NOTIFICATION_TIMEOUT_LONG,
                )

    def handle_mutex(self) -> None:
        try:
            self.mutex = win32event.CreateMutex(None, False, APP_NAME)
            if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
                self.notify_instance_already_running()
                os._exit(1)
        except Exception as e:
            notify(
                "Error",
                f"Error creating mutex: {e}",
                NOTIFICATION_TIMEOUT_LONG,
            )
            os._exit(1)

    def handle_lock_file(self) -> None:
        lock_file = "/tmp/clipboardlistener.lock"
        try:
            self.lock_fd = os.open(lock_file, os.O_CREAT | os.O_EXCL | os.O_RDWR)
        except OSError:
            self.notify_instance_already_running()
            os._exit(1)
        else:
            fcntl.flock(self.lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)

    def notify_instance_already_running(self) -> None:
        notify(
            "Instance Running",
            "An instance of Gramma is already running.",
            NOTIFICATION_TIMEOUT_LONG,
        )

    def cleanup(self) -> None:
        if sys.platform.startswith("win"):
            win32event.ReleaseMutex(self.mutex)
        else:
            if fcntl is not None:
                os.close(self.lock_fd)
                os.unlink("/tmp/clipboardlistener.lock")
