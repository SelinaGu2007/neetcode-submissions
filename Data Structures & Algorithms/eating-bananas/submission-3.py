class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = None

        while left < right:
            middle = (left + right) // 2
            hours = 0
            for num in piles:
                hours += (num - 1) // middle + 1
            if hours <= h:
                right = middle
            else:
                left = middle + 1

        return left