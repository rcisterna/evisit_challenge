class Tracker:
    """Static class that tracks handled requests."""

    @staticmethod
    def request_handled(ip: str):
        """
        Add handled request.

        This function accepts a string containing an IP address like “145.87.2.109”.
        This function will be called by the web service every time it handles a request.
        The calling code is outside the scope of this project.
        Since it is being called very often, this function needs to have a fast runtime.
        """

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

    @staticmethod
    def clear():
        """
        Clear stored data.

        Called at the start of each day to forget about all IP addresses and tallies.
        """
