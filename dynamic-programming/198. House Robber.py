from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def maxSum(n):
            if n in dp:
                return dp[n]
            if n == len(nums) - 1:
                return nums[n]
            if n == len(nums):
                return 0

            pick = nums[n] + maxSum(n + 2)
            notPick = 0 + maxSum(n + 1)
            maximum = max(pick, notPick)
            dp[n] = maximum
            return maximum

        return maxSum(0)


sol = Solution()

print(sol.rob([1, 2, 3, 1]))
print(sol.rob([2, 7, 9, 3, 1]))
print(sol.rob([]))
