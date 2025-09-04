from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digits = [int(digit) for digit in digits]
        if len(digits) == 0 or 0 in digits or 1 in digits:
            return []
        lettermap = [
            [],
            [],
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
            ["m", "n", "o"],
            ["p", "q", "r", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"],
        ]

        def _combinations(startdigit, output):
            if len(output) == len(digits):
                res.append(output[:])
                return
            for i in range(len(lettermap[digits[startdigit]])):
                output.append(lettermap[digits[startdigit]][i])
                _combinations(startdigit + 1, output)
                output.pop()

        _combinations(0, [])
        res = ["".join(item) for item in res]
        return res

    ######## DO LOOK AT THIS MORE IMPROVED VERSION. THE ABOVE ONE WAS WRITTEN BY ME BUT THIS ONE IS AI GENERATED ##########

    def improved(digits: str):
        if not digits or "0" in digits or "1" in digits:
            return []

        lettermap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append(path)
                return
            for ch in lettermap[digits[index]]:
                backtrack(index + 1, path + ch)

        backtrack(0, "")
        return res


sol = Solution()
print(sol.letterCombinations("234"))
