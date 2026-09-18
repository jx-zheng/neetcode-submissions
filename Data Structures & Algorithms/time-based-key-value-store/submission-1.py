from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.internal_map = defaultdict(list) # string -> list of tuples (time, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.internal_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.internal_map[key]
        if not values:
            return ""

        l, r = 0, len(values) - 1

        while l < r:
            mid = (l + r + 1) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            if values[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid

        # check again
        if values[l][0] <= timestamp:
            return values[l][1]
        else:
            return ""
