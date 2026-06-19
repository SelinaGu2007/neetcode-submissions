class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]

        out = [[]]
        for i in range(len(nums)):
            rest = self.subsets(nums[i + 1:])
            for subset in rest:
                out.append(subset + [nums[i]])

        return out