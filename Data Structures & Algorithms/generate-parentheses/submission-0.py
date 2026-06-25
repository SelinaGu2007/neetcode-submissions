class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ""

        def dfs(left, right):
            nonlocal path
            if left == n and right == n:
                res.append(path)
                return 

            if left > n or left < right:
                return

            path += "("
            dfs(left + 1, right)
            path = path[:-1]
            path += ")"
            dfs(left, right + 1)
            path = path[:-1]

        dfs(0, 0)

        return res