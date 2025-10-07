# User function Template for python3

from typing import List


class Solution:

    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        # code here

        memo = {}

        def dfs(curr):
            if curr in memo:
                return memo[curr]

            if curr == end:
                return 0

            if curr > end:
                return float("inf")

            best = float("inf")
            for num in arr:
                steps = 1 + dfs(curr * num)
                best = min(best, steps)

            memo[curr] = best
            return best

        ans = dfs(start)
        return ans if ans != float("inf") else -1


sol = Solution()

print(sol.minimumMultiplications([2, 5, 7], 3, 30))  # 2
# print(sol.minimumMultiplications([3, 4, 65], 7, 66175))  # 4
