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

        def dfs(i, cur):

            if i == len(word):
                return cur.isWord

            if word[i] != "." and word[i] not in cur.children:
                return False

            if word[i] != ".":
                return dfs(i + 1, cur.children[word[i]])

            else:
                for child in cur.children.keys():
                    if dfs(i + 1, cur.children[child]):
                        return True

                return False

        return dfs(0, self.root)