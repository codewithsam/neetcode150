# https://github.com/doocs/leetcode/blob/main/solution/1800-1899/1858.Longest%20Word%20With%20All%20Prefixes/README_EN.md?utm_source=chatgpt.com

from typing import List


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
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.eow = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            idx = ord(ch) - self.base
            curr = curr.children[idx]
            if not curr.eow:
                return False
        return True


class Solution:
    def longestPrefix(self, words: List[str]) -> str:
        trie = Trie()
        ans = ""
        for w in words:
            trie.insert(w)
            if trie.search(w):
                if len(w) > len(ans):
                    ans = w
                elif len(w) == len(ans) and w < ans:  # same length -> lexicographically smaller
                    ans = w

        return ans


sol = Solution()
print(sol.longestPrefix(["a", "ap", "app", "appl", "apple"]))
