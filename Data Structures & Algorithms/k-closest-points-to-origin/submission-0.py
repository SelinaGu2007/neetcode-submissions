class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = (x**2 + y**2) ** 0.5
            dist.append((distance, x, y))

        heapq.heapify(dist)

        res = []
        for i in range(k):
            _, x, y = heapq.heappop(dist)
            res.append([x, y])

        return res