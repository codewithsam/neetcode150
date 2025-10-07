from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0

        def _dfs(r, c):
            nonlocal count
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return
            count += 1
            grid[r][c] = 2
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                _dfs(r + dr, c + dc)

        for row in range(rows):
            for col in range(cols):
                count = 0
                if grid[row][col] == 1:
                    _dfs(row, col)
                    area = max(area, count)
        return area


sol = Solution()

print(sol.maxAreaOfIsland([[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]))


################################### ANOTHER WAY TO DO THE DFS WITHOUT NONLOCAL


class SolutionWithoutNonLocal:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0

        def _dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = 2
            count = 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                count += _dfs(r + dr, c + dc)
            return count

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = max(area, _dfs(row, col))
        return area


sol2 = SolutionWithoutNonLocal()

print(sol2.maxAreaOfIsland([[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]))
