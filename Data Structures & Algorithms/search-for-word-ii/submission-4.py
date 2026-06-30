class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        root = TrieNode()

        for word in words:
            cur = root
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]

            cur.word = word

        res = []

        def dfs(row, col, cur):

            if row < 0 or row >= n or col < 0 or col >= m:
                return 

            letter = board[row][col]

            if letter == "#" or letter not in cur.children:
                return

            cur = cur.children[letter]
            board[row][col] = "#"

            if cur.word:
                res.append(cur.word)
                cur.word = None

            dfs(row - 1, col, cur)
            dfs(row + 1, col, cur)
            dfs(row, col - 1, cur)
            dfs(row, col + 1, cur)

            board[row][col] = letter

        for i in range(n):
            for j in range(m):
                if board[i][j] in root.children:
                    dfs(i, j, root)

        return res