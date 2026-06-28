class Solution:
    def isPalindrome(self, s, i, j):
        if i >= j:
            return True

        if s[i] == s[j] and self.isPalindrome(s, i + 1, j - 1):
            return True

        return False

    def partition(self, s: str) -> List[List[str]]:
        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    dp[i][j] = True

        part = []
        res = []

        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if dp[i][j]:
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)

        return res