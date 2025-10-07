from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(targetSum, memo={}):
            if targetSum in memo:
                return memo[targetSum]
            if targetSum == 0:
                return [[]]
            if targetSum < 0:
                return []

            res = []
            for candidate in candidates:
                for combo in backtrack(targetSum - candidate):
                    res.append(combo + [candidate])
            memo[targetSum] = res
            return res

        return backtrack(target)


sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
