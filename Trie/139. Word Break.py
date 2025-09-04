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


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        memo = {}
        for word in wordDict:
            trie.insert(word)

        def _wordBreak(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            curr = trie.root
            for i in range(start, len(s)):
                idx = ord(s[i]) - ord("a")
                if curr.children[idx] is None:
                    break
                curr = curr.children[idx]
                if curr.eow == True and _wordBreak(i + 1):
                    memo[start] = True
                    return True
            memo[start] = False
            return False

        return _wordBreak(0)


sol = Solution()
print(sol.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]))
print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(sol.wordBreak("aaaaaaa", ["a", "aa", "aaa", "aaaa"]))
