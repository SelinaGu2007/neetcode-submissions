class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)

        total_left = (l1 + l2) // 2 + 1
        i = -1
        j = -1
        median1 = None
        median2 = None
        while (i + j + 2) < total_left:
            num1 = float('inf') if i >= l1 - 1 else nums1[i + 1]
            num2 = float('inf') if j >= l2 - 1 else nums2[j + 1]
            if num1 <= num2:
                i += 1
                median2 = median1
                median1 = num1
            else:
                j += 1
                median2 = median1
                median1 = num2

        if (l1 + l2) % 2 == 1:
            return median1
        else:
            return (median1 + median2) / 2