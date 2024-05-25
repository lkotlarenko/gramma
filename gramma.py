import os
import threading
from src.data import SharedData
from src.core.clipboard_listener import ClipboardListener
from src.core.tray_icon import TrayIcon
from src.managers.instance_manager import InstanceManager


def main():
    instance_manager = InstanceManager()
    shared_data = SharedData()
    listener = ClipboardListener(shared_data)
    TrayIcon(listener)

    try:
        listener_thread = threading.Thread(target=listener.monitor_clipboard)
        listener_thread.start()
    except KeyboardInterrupt:
        listener.stop_monitoring()
    except Exception as e:
        print(f"An error occurred: {e}")
        listener.stop_monitoring()
    finally:
        instance_manager.cleanup()
        os._exit(0)


if __name__ == "__main__":
    main()
