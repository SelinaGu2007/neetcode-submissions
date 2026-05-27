class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return -1

        left = 1
        right = max(piles)
        ans = None

        while left <= right:
            middle = (left + right) // 2
            hours = 0
            for num in piles:
                hours += (num - 1) // middle + 1
            if hours <= h:
                right = middle - 1
                ans = middle
            else:
                left = middle + 1

        if ans:
            return ans
        return -1