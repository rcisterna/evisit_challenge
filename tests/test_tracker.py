from requests_tracker import Tracker


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
