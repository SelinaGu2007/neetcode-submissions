class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        n = len(height)

        for i in range(n):
            while stack and height[i] >= height[stack[-1]]:
                bottom = stack.pop()
                if stack:
                    left = stack[-1]
                    h = min(height[i], height[left])
                    res += (i - left - 1) * (h - height[bottom])

            stack.append(i)

        return res