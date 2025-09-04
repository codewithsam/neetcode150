class Node:
    def __init__(self):
        self.children = [None] * 26
        self.eow = False


class Trie:
    def __init__(self):
        self.root = Node()
        self.base = ord("a")

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            idx = ord(ch) - self.base
            if curr.children[idx] == None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.eow = True

    def search(self, word: str) -> bool:
        def _search(i, node):
            if node is None:
                return False

            if i == len(word):
                return node.eow

            ch = word[i]

            if ch == ".":
                for child in node.children:
                    if child and _search(i + 1, child):
                        return True
                return False
            return _search(i + 1, node.children[ord(ch) - self.base])

        return _search(0, self.root)


wordDictionary = Trie()

wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))  # return False
print(wordDictionary.search("bad"))  # return True
print(wordDictionary.search(".ad"))  # return True
print(wordDictionary.search("b.."))  # return True
