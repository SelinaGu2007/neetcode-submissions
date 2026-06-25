class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = ""
        n = len(board)
        m = len(board[0])

        def dfs(i, j):
            nonlocal path

            if len(path) == len(word):
                return True

            if i < 0 or i >= n or j < 0 or j >= m:
                return False

            if board[i][j] != word[len(path)]:
                return False

            path += board[i][j]
            temp = board[i][j]
            board[i][j] = "#"
            res = dfs(i+1, j) or dfs(i-1, j) or dfs(i, j-1) or dfs(i, j+1)
            path = path[:-1]
            board[i][j] = temp
            return res

        for i in range(n):
            for j in range(m):
                if dfs(i, j):
                    return True

        return False