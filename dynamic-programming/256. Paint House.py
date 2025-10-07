# leetcode number is 256 but is a premium problem. https://leetcode.com/problems/paint-house/description/
# On lintcode we have a link -> https://www.lintcode.com/problem/515/description


from typing import (
    List,
)


class Solution:
    def min_cost(self, costs: List[List[int]]) -> int:
        dp = [[float("inf") for _ in range(len(costs[0]))] for _ in range(len(costs))]
        if len(costs) == 0:
            return 0

        def findMin(house, lastColor):
            if lastColor != 3 and dp[house][lastColor] != float("inf"):
                return dp[house][lastColor]

            if house == 0:
                total = float("inf")
                for colorIdx in range(len(costs[0])):
                    if colorIdx != lastColor:
                        total = min(total, costs[0][colorIdx])
                return total

            minCost = float("inf")
            for colorIdx in range(len(costs[house])):
                points = 0
                if colorIdx != lastColor:
                    points += costs[house][colorIdx] + findMin(house - 1, colorIdx)
                    minCost = min(minCost, points)
            if lastColor != len(costs[0]):
                dp[house][lastColor] = minCost
            return minCost

        return findMin(len(costs) - 1, 3)

    def min_cost_tab(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        nColors = len(costs[0])
        dp = [[float("inf")] * nColors for _ in range(len(costs))]

        dp[0] = costs[0][:]
        """
        you don't really need to store a 2d array pertaining all pre-calculated values. you can just have 1 list of 3 values
        Every time you move to new house save all calulates of previous row since that is what really matters.
        I have not shown that solution here but for future reference. We can go ahead and ask chatgpt for that
        """

        for house in range(1, len(costs)):
            for colorIdx in range(nColors):
                dp[house][colorIdx] = float("inf")
                prevMin = float("inf")
                for prevCols in range(nColors):
                    if prevCols != colorIdx:
                        prevMin = min(prevMin, dp[house - 1][prevCols])
                dp[house][colorIdx] = costs[house][colorIdx] + prevMin
        return min(dp[-1])


sol = Solution()
print(sol.min_cost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))  # Expected: 10
print(sol.min_cost([[7, 6, 2]]))  # Expected: 2
print(sol.min_cost([]))  # Expected: 0
print(sol.min_cost([[1, 100, 100], [100, 1, 100]]))  # Expected: 2
print(sol.min_cost([[5, 8, 6], [1, 3, 2]]))  # Expected: 7
print(sol.min_cost([[10, 5, 20], [3, 30, 100], [50, 20, 2], [1, 100, 50]]))  # Example large
print(sol.min_cost([[5, 5, 5], [5, 5, 5], [5, 5, 5]]))  # Expected: 15


print(sol.min_cost_tab([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))  # Expected: 10
print(sol.min_cost_tab([[7, 6, 2]]))  # Expected: 2
print(sol.min_cost_tab([]))  # Expected: 0
print(sol.min_cost_tab([[1, 100, 100], [100, 1, 100]]))  # Expected: 2
print(sol.min_cost_tab([[5, 8, 6], [1, 3, 2]]))  # Expected: 7
print(sol.min_cost_tab([[10, 5, 20], [3, 30, 100], [50, 20, 2], [1, 100, 50]]))  # Example large
print(sol.min_cost_tab([[5, 5, 5], [5, 5, 5], [5, 5, 5]]))  # Expected: 15
