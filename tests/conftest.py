import pytest

from src.core.clipboard_listener import ClipboardListener
from src.data import SharedData


@pytest.fixture
def shared_data():
    return SharedData()


@pytest.fixture
def listener(shared_data):
    return ClipboardListener(shared_data)


def create_shared_data():
    return SharedData()


def create_listener(shared_data):
    return ClipboardListener(shared_data)
