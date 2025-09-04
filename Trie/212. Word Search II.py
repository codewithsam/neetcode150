from typing import List


class Node:
    def __init__(self):
        self.children = [None] * 26
        self.eow = False


class Trie:
    def __init__(self):
        self.root = Node()
        self.base = ord("a")

    def insert(self, word: str):
        curr = self.root
        for ch in word:
            idx = ord(ch) - self.base
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
        curr.eow = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        res = []
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c, word, node):
            if r < 0 or c < 0 or r >= rows or c >= cols or visited[r][c]:
                return False

            idx = ord(board[r][c]) - trie.base

            if node.children[idx] is None:
                return

            visited[r][c] = True
            node = node.children[idx]
            word += board[r][c]
            if node.eow:
                res.append(word)
                node.eow = False

            dfs(r + 1, c, word, node)
            dfs(r - 1, c, word, node)
            dfs(r, c + 1, word, node)
            dfs(r, c - 1, word, node)
            visited[r][c] = False

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, "", trie.root)
        return res


sol = Solution()

board = [["a", "b", "c", "d"], ["s", "a", "a", "t"], ["a", "c", "k", "e"], ["a", "c", "d", "n"]]
words = ["bat", "cat", "back", "backend", "stack"]

print(sol.findWords(board, words))
