from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(substr, start, end):
            while start < end:
                if substr[start] != substr[end]:
                    return False
                start, end = start + 1, end - 1
            return True

        def _partition(start, output):
            if start >= len(s):
                res.append(output.copy())
            for end in range(start, len(s)):
                if isPalindrome(s, start, end):
                    output.append(s[start : end + 1])
                    _partition(end + 1, output)
                    output.pop()

        _partition(0, [])
        return res


sol = Solution()

print(sol.partition("aab"))
print(sol.partition("racecar"))
