class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        left1 = 0
        right1 = left - 1
        left2 = left
        right2 = len(nums) - 1

        if target > nums[-1]:
            while left1 <= right1:
                middle1 = (left1 + right1) // 2
                if nums[middle1] == target:
                    return middle1
                elif nums[middle1] > target:
                    right1 = middle1 - 1
                else:
                    left1 = middle1 + 1

        else:
            while left2 <= right2:
                middle2 = (left2 + right2) // 2
                if nums[middle2] == target:
                    return middle2
                elif nums[middle2] > target:
                    right2 = middle2 - 1
                else:
                    left2 = middle2 + 1

        return -1