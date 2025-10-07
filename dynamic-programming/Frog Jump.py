## https://www.geeksforgeeks.org/problems/geek-jump/1


class Solution:
    def minCost(self, height):
        numlen = len(height)
        dp = [-1 for _ in range(numlen)]

        def totalCost(n):
            if n == 0:
                return 0

            if dp[n] != -1:
                return dp[n]

            left = totalCost(n - 1) + abs(height[n] - height[n - 1])
            right = float("inf")
            if n > 1:
                right = totalCost(n - 2) + abs(height[n] - height[n - 2])

            dp[n] = min(left, right)
            return dp[n]

        return totalCost(numlen - 1)


sol = Solution()

print(sol.minCost([20, 30, 40, 20]))  # 20
print(sol.minCost([30, 20, 50, 10, 40]))  # 30
print(sol.minCost([10, 30, 40, 20, 50]))  # 40
