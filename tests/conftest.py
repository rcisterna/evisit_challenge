import random
import socket
import struct

import pytest
from requests_tracker import Tracker


def get_random_ip():
    return socket.inet_ntoa(struct.pack(">I", random.randint(1, 0xFFFFFFFF)))


@pytest.fixture
def reset_tracker():
    Tracker.clear()


@pytest.fixture
def random_ip():
    return get_random_ip()
