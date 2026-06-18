class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = min(nums)
        r = max(nums)

        while l < r:
            mid = (l + r) // 2
            m = 0
            for num in nums:
                if num > mid:
                    m += 1

            if m >= k:
                l = mid + 1
            else:
                r = mid

        return l