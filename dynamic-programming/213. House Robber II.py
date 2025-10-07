from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def maxSum(start, end):
            dp = {}

            def helper(n):
                if n in dp:
                    return dp[n]
                if n == end - 1:
                    return nums[n]
                if n == end:
                    return 0

                pick = nums[n] + helper(n + 2)
                notPick = 0 + helper(n + 1)
                maximum = max(pick, notPick)
                dp[n] = maximum
                return maximum

            return helper(start)

        return max(maxSum(0, len(nums) - 1), maxSum(1, len(nums)))


sol = Solution()

print(sol.rob([2, 3, 2]))
print(sol.rob([1, 2, 3, 1]))
print(sol.rob([1, 2, 3]))
