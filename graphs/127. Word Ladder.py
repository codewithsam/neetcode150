from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append(beginWord)
        count = 0
        wordset = set(wordList)

        while q:
            count += 1
            width = len(q)
            for _ in range(width):
                word = q.popleft()
                if word == endWord:
                    return count
                for cidx in range(len(word)):
                    for pos in range(26):
                        nword = word[:cidx] + chr(pos + ord("a")) + word[cidx + 1 :]
                        if nword in wordset:
                            wordset.remove(nword)
                            q.append(nword)
        return 0


sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
