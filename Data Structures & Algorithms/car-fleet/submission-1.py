class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pos_speed = []
        for i in range(n):
            pos_speed.append((position[i], speed[i]))
        pos_speed_sort = sorted(pos_speed)

        times = []
        for i in range(n):
            dist = target - pos_speed_sort[i][0]
            time = dist / pos_speed_sort[i][1]
            times.append(time)

        fleet = 1
        cur = times[-1]
        for i in range(n-2, -1, -1):
            if times[i] > cur:
                fleet += 1
                cur = times[i]

        return fleet