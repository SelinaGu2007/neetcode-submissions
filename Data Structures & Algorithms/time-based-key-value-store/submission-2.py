class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        if self.timeMap[key]:
            times = sorted(self.timeMap[key].keys())
            l = 0
            r = len(times) - 1
            while l <= r:
                m = (l + r) // 2
                if times[m] > timestamp:
                    r = m - 1
                else:
                    res = self.timeMap[key][times[m]]
                    l = m + 1

        return res
