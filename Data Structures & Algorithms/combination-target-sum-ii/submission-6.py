class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        count = defaultdict(int)
        for cand in candidates:
            count[cand] += 1
        A = list(count.keys())

        res = []
        
        def dfs(i, cur, s):
            if s == target:
                res.append(cur.copy())
                return

            if s > target or i == len(A):
                return

            if count[A[i]] > 0:
                cand = A[i]
                cur.append(cand)
                count[cand] -= 1
                dfs(i, cur, s + cand)
                count[cand] += 1
                cur.pop()

            dfs(i+1, cur, s)

        dfs(0, [], 0)

        return res