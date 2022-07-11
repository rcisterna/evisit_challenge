class Tracker:
    """Static class that tracks handled requests."""
    _counts_by_addr = {}  # hash table with requests count, indexed by ip address
    _addrs_by_count = {}  # hash table with list of addresses, indexed by requests count
    _sorted_counts = []  # list with ordered requests count in descending order

    @staticmethod
    def request_handled(ip: str):
        """
        Add handled request.

        This function accepts a string containing an IP address like “145.87.2.109”.
        This function will be called by the web service every time it handles a request.
        The calling code is outside the scope of this project.
        Since it is being called very often, this function needs to have a fast runtime.
        """
        count = Tracker._counts_by_addr.get(ip, 0)
        if count > 0:
            Tracker._addrs_by_count[count].pop(ip)
            if not Tracker._addrs_by_count[count]:
                Tracker._addrs_by_count.pop(count)

        count += 1
        Tracker._counts_by_addr[ip] = count
        if count in Tracker._addrs_by_count:
            Tracker._addrs_by_count[count].append(ip)
        else:
            Tracker._addrs_by_count[count] = [ip]

        Tracker._sorted_counts = sorted(Tracker._addrs_by_count.keys(), reverse=True)

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
        for count in Tracker._sorted_counts:
            len_addrs = len(addrs)
            if len_addrs == 100:
                break
            truncate = None
            if len_addrs + count > 100:
                truncate = 100 - len_addrs
            to_append = Tracker._addrs_by_count[count]
            addrs.extend(to_append[:truncate])
        return addrs

    @staticmethod
    def clear():
        """
        Clear stored data.

        Called at the start of each day to forget about all IP addresses and tallies.
        """
        Tracker._counts_by_addr.clear()
        Tracker._addrs_by_count.clear()
        Tracker._sorted_counts.clear()
