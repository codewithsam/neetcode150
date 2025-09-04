class Node:
    def __init__(self):
        self.children = [None] * 26
        self.eow = False


class Trie:

    def __init__(self):
        self.root = Node()
        self.base = ord("a")

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            idx = ord(ch) - self.base
            if curr.children[idx] == None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.eow = True

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            idx = ord(ch) - self.base
            curr = curr.children[idx]
            if curr is None:
                return False
        return curr.eow

        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            idx = ord(ch) - self.base
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
