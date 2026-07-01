class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        max_area = 0
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0

            if (i, j) in visited:
                return 0

            if grid[i][j] == 0:
                return 0

            visited.add((i, j))

            a1 = dfs(i - 1, j)
            a2 = dfs(i + 1, j)
            a3 = dfs(i, j - 1)
            a4 = dfs(i, j + 1)

            return a1 + a2 + a3 + a4 + 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(dfs(i, j), max_area)

        return max_area