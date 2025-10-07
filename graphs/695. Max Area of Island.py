from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        output = 0

        def _dfs(row, col):
            if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            return 1 + _dfs(row + 1, col) + _dfs(row - 1, col) + _dfs(row, col + 1) + _dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    output = max(output, _dfs(row, col))
        return output


sol = Solution()
print(sol.maxAreaOfIsland([[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]))
