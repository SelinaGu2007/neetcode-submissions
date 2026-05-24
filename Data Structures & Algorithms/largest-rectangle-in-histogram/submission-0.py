class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            area = heights[i]
            k1 = i - 1
            k2 = i + 1
            while k1 >= 0 and heights[k1] >= heights[i]:
                area += heights[i]
                k1 -= 1
            while k2 <= n - 1 and heights[k2] >= heights[i]:
                area += heights[i]
                k2 += 1
            max_area = max(area, max_area)

        return max_area