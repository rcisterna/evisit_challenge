import pytest
from requests_tracker import Tracker


@pytest.fixture
def reset_tracker():
    Tracker.clear()
