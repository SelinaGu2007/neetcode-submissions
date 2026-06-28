class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(start, s):
            if s == target:
                res.append(path.copy())
                return 

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if s + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, s + candidates[i])
                path.pop()

        dfs(0, 0)

        return res