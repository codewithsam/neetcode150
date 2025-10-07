from typing import List


class Solution:
    def dp(self, cost: List[int]) -> int:
        prev1, prev2, total = cost[1], cost[0], 0

        for i in range(2, len(cost)):
            total = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = total
        return min(prev2, prev1)

    def topDown(self, cost: List[int]) -> int:
        dp = [-1 for _ in range(len(cost))]
        n = len(cost)

        def minCost(n):
            if dp[n] != -1:
                return dp[n]
            if n < 0:
                return 0
            if n == 0 or n == 1:
                return cost[n]

            dp[n] = cost[n] + min(minCost(n - 1), minCost(n - 2))
            return dp[n]

        return min(minCost(n - 1), minCost(n - 2))


sol = Solution()

# print(sol.dp([10, 15, 20]))  # expected 15
# print(sol.dp([1, 100, 1, 150, 1, 100, 1, 1, 100, 1]))  # expected 6
# print(sol.dp([0, 0, 0, 0]))  # expected 0
# print(sol.dp([5, 10, 5]))  # expected 5
# print(sol.dp([10, 15, 5, 10, 20]))  # some non-trivial mix
# print(sol.dp([1, 2]))  # minimal size
# print(sol.dp([1000, 1, 1, 1, 1, 1000]))  # edge with big and small costs


print(sol.topDown([10, 15, 20]))  # expected 15
print(sol.topDown([1, 100, 1, 150, 1, 100, 1, 1, 100, 1]))  # expected 6
print(sol.topDown([0, 0, 0, 0]))  # expected 0
print(sol.topDown([5, 10, 5]))  # expected 5
print(sol.topDown([10, 15, 5, 10, 20]))  # some non-trivial mix
print(sol.topDown([1, 2]))  # minimal size
print(sol.topDown([1000, 1, 1, 1, 1, 1000]))  # edge with big and small costs
