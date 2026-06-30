class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

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

            cur.isWord = True

        res = set()
        visited = set()

        def dfs(row, col, word, cur):

            if row < 0 or row >= n or col < 0 or col >= m or (row, col) in visited:
                return 

            if board[row][col] not in cur.children:
                return

            letter = board[row][col]
            cur = cur.children[letter]
            word += letter
            visited.add((row, col))

            if cur.isWord:
                res.add(word)

            dfs(row - 1, col, word, cur)
            dfs(row + 1, col, word, cur)
            dfs(row, col - 1, word, cur)
            dfs(row, col + 1, word, cur)

            visited.discard((row, col))

        for i in range(n):
            for j in range(m):
                dfs(i, j, '', root)

        return list(res)