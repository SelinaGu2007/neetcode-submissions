class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]

        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(i):
            nonlocal cur

            if i == len(word):
                return cur.isWord

            if word[i] != "." and word[i] not in cur.children:
                return False

            if word[i] != ".":
                cur = cur.children[word[i]]
                return dfs(i + 1)

            else:
                current = cur
                for child in current.children.keys():
                    cur = current.children[child]
                    if dfs(i + 1):
                        return True

                return False

        return dfs(0)