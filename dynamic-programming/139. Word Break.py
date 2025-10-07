from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def backtrack(idx, memo={}):
            if idx in memo:
                return memo[idx]
            if idx == len(s):
                return True

            for word in wordDict:
                wordLen = len(word)
                wordIdx = 0
                for i in range(idx, len(s)):
                    if s[i] != word[wordIdx]:
                        break
                    wordIdx += 1
                    if wordIdx == wordLen:
                        break
                if wordIdx == wordLen:
                    if backtrack(i + 1):
                        memo[idx] = True
                        return True
            memo[idx] = False
            return False

        return backtrack(0)


sol = Solution()

print(sol.wordBreak("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(sol.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]))
print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(sol.wordBreak("aaaaaaa", ["a", "aa", "aaa", "aaaa"]))
print(sol.wordBreak("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eeee", "eeeeeeeeee"]))


##########################################  SOLUTION YOU CAN BUILD WHERE #########################################
# ###################################  YOU DON't HAVE TO ITERATE AND CHECK FOR SUBSTRING  ########################


class SolutionWithBuiltInPythonFunction:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def backtrack(idx, memo={}):
            if idx in memo:
                return memo[idx]
            if idx == len(s):
                return True

            for word in wordDict:
                if s.startswith(word, idx):
                    if backtrack(idx + len(word)):
                        memo[idx] = True
                        return True
            memo[idx] = False
            return False

        return backtrack(0)
