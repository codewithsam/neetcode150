from typing import List


class Solution:
    def bestSum(self, candidates: List[int], target: int) -> List[int]:
        def backtrack(targetSum, memo={}):
            if targetSum in memo:
                return memo[targetSum]
            if targetSum == 0:
                return []
            if targetSum < 0:
                return None
            minCombos = None
            for candidate in candidates:
                remainder = targetSum - candidate
                combos = backtrack(remainder, memo)
                if combos is not None:
                    currentCombo = combos + [candidate]
                    if minCombos is None or len(currentCombo) < len(minCombos):
                        minCombos = currentCombo
            memo[targetSum] = minCombos
            return minCombos

        return backtrack(target)


sol = Solution()

print(sol.bestSum([5, 3, 4, 7], 7))
print(sol.bestSum([2, 3, 5], 8))
print(sol.bestSum([1, 4, 5], 8))
print(sol.bestSum([1, 2, 5, 25], 100))
