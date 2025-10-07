from typing import List


class Solution:
    def maximumSumSubsequence(self, arr: List[int]) -> int:
        dp = {}

        def maxSum(n):
            if n in dp:
                return dp[n]
            if n == len(arr) - 1:
                return arr[n]
            if n == len(arr):
                return 0

            pick = arr[n] + maxSum(n + 2)
            notPick = 0 + maxSum(n + 1)
            maximum = max(pick, notPick)
            dp[n] = maximum
            return maximum

        return maxSum(0)


sol = Solution()

print(sol.maximumSumSubsequence([5, 5, 10, 100, 10, 5]))  # 110
print(sol.maximumSumSubsequence([3, 2, 7, 10]))  # 13
print(sol.maximumSumSubsequence([9, 1, 6, 10]))  # 19
