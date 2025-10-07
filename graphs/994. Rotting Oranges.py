from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
        time = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # Spread only to fresh oranges
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # fresh → rotten
                        q.append((nr, nc))
            if q:  # Only increment time if new oranges rotted this round
                time += 1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return time


sol = Solution()

print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(sol.orangesRotting([[0, 2]]))
