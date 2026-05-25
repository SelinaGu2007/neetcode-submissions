class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        right = 0
        res = []

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)
            if right >= k - 1:
                while q[0] <= right - k:
                    q.popleft()
                res.append(nums[q[0]])
            right += 1

        return res
