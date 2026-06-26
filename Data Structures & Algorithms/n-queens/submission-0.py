class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = [["."] * n for _ in range(n)]
        used_col = set()
        used_diag_s = set() 
        used_diag_d = set()
        
        def dfs(row):
            nonlocal used_col, used_diag_s, used_diag_d

            if row == n:
                res.append(["".join(row) for row in path])
                return

            for col in range(n):
                s = row + col
                d = row - col

                if col in used_col or s in used_diag_s or d in used_diag_d:
                    continue

                path[row][col] = "Q"

                used_col.add(col)
                used_diag_s.add(s)
                used_diag_d.add(d)

                dfs(row + 1)

                path[row][col] = "."

                used_col.remove(col)
                used_diag_s.remove(s)
                used_diag_d.remove(d)

        dfs(0)

        return res