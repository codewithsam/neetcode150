from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def _generate_combinations(open, close, combination, n):
            nonlocal res
            if len(combination) >= 2*n:
                res.append("".join(combination))
                return
            if open > 0:
                combination.append("(")
                _generate_combinations(open - 1, close, combination, n)
                combination.pop()

            if close > open:
                combination.append(")")
                _generate_combinations(open, close-1, combination, n)
                combination.pop()
        _generate_combinations(n,n,[], n)
        return res

sol = Solution()

print(sol.generateParenthesis(1))
print(sol.generateParenthesis(2))
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(4))
