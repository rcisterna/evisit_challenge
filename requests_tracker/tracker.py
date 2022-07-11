class Tracker:
    """Static class that tracks handled requests."""
    reqs_by_addr = {}  # hash table with requests count, indexed by ip address
    addrs_by_req = {}  # hash table with list of addresses, indexed by requests count
    sorted_req_counts = []  # list with ordered requests count in descending order

    @staticmethod
    def request_handled(ip: str):
        """
        Add handled request.

        This function accepts a string containing an IP address like “145.87.2.109”.
        This function will be called by the web service every time it handles a request.
        The calling code is outside the scope of this project.
        Since it is being called very often, this function needs to have a fast runtime.
        """
        reqs_count = Tracker.reqs_by_addr.get(ip, 0)
        if reqs_count > 0:
            Tracker.addrs_by_req[reqs_count].pop(ip)
            if not Tracker.addrs_by_req[reqs_count]:
                Tracker.addrs_by_req.pop(reqs_count)

        reqs_count += 1
        Tracker.reqs_by_addr[ip] = reqs_count
        if reqs_count in Tracker.addrs_by_req:
            Tracker.addrs_by_req[reqs_count].append(ip)
        else:
            Tracker.addrs_by_req[reqs_count] = [ip]

        Tracker.sorted_req_counts = sorted(Tracker.addrs_by_req.keys(), reverse=True)

    @staticmethod
    def top100():
        """
        Get top 100 IP addresses by request count.

        This function should return the top 100 IP addresses by request count, with the
        highest traffic IP address first.
        This function also needs to be fast.
        Imagine it needs to provide a quick response (< 300ms) to display on a
        dashboard, even with 20 millions IP addresses. This is a very important
        requirement. Don’t forget to satisfy this requirement.
        """
        addrs = []
        for counts in Tracker.sorted_req_counts:
            len_addrs = len(addrs)
            if len_addrs == 100:
                break
            truncate = None
            if len_addrs + counts > 100:
                truncate = 100 - len_addrs
            new_addrs = Tracker.sorted_req_counts[counts]
            addrs.extend(new_addrs[:truncate])
        return addrs

    @staticmethod
    def clear():
        """
        Clear stored data.

        Called at the start of each day to forget about all IP addresses and tallies.
        """
        Tracker.reqs_by_addr.clear()
        Tracker.addrs_by_req.clear()
        Tracker.sorted_req_counts.clear()
