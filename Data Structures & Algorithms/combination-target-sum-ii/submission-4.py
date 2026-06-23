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
                if s > target:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                s += candidates[i]
                dfs(i + 1, s)
                path.pop()
                s -= candidates[i]

        dfs(0, 0)

        return res