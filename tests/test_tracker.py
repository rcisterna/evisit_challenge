import time

import pytest
from requests_tracker import Tracker

from .conftest import get_random_ip


def test_add_single_ip(reset_tracker, random_ip):
    Tracker.request_handled(random_ip)
    assert Tracker._counts_by_addr == {random_ip: 1}
    assert Tracker._addrs_by_count == {1: [random_ip]}
    assert Tracker._sorted_counts == [1]


def test_add_duplicated_ip(reset_tracker, random_ip):
    Tracker.request_handled(random_ip)
    Tracker.request_handled(random_ip)
    assert Tracker._counts_by_addr == {random_ip: 2}
    assert Tracker._addrs_by_count == {2: [random_ip]}
    assert Tracker._sorted_counts == [2]


def test_clear(reset_tracker, random_ip):
    Tracker.request_handled(random_ip)
    Tracker.clear()
    assert Tracker._counts_by_addr == {}
    assert Tracker._addrs_by_count == {}
    assert Tracker._sorted_counts == []


@pytest.mark.parametrize(
    "counts_by_ips",
    [
        {get_random_ip(): 1000, get_random_ip(): 10000, get_random_ip(): 5000},
        {get_random_ip(): i * 100000 for i in range(1, 21)},
    ],
)
def test_performance(reset_tracker, counts_by_ips):
    for ip, count in counts_by_ips.items():
        for _ in range(count):
            Tracker.request_handled(ip)
    start = time.time()
    Tracker.top100()
    end = time.time()
    assert Tracker._counts_by_addr == counts_by_ips
    assert Tracker._addrs_by_count == {c: [ip] for ip, c in counts_by_ips.items()}
    assert Tracker._sorted_counts == sorted(counts_by_ips.values(), reverse=True)
    assert end - start < 0.3
