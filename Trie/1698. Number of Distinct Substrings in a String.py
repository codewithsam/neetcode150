from collections import deque


class Node:
    def __init__(self):
        self.children = [None] * 26
        self.eow = False


class Trie:
    def __init__(self):
        self.root = Node()
        self.base = ord("a")

    def insert(self, word):
        curr = self.root
        for ch in word:
            idx = ord(ch) - self.base
            if curr.children[idx] == None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.eow = True


class Solution:
    def substrings(self, s: str) -> int:
        trie = Trie()
        for i in range(len(s)):
            trie.insert(s[i:])

        count = 1
        root = trie.root
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            for i in range(len(node.children)):
                if node.children[i] is not None:
                    count += 1
                    q.append(node.children[i])

        return count


sol = Solution()
print(sol.substrings("ababa"))
