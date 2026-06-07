class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if key == self.cache[i][0]:
                value = self.cache[i][1]
                self.cache.pop(i)
                self.cache.append((key, value))
                return value

        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if key == self.cache[i][0]:
                self.cache.pop(i)
                self.cache.append((key, value))
                return

        if len(self.cache) == self.capacity:
            self.cache.pop(0)
        self.cache.append((key, value))
