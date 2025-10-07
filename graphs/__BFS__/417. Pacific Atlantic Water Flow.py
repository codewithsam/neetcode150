from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                visited.add((r, c))
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))
            return visited

        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        pacific_reach = bfs(pacific_starts)
        atlantic_reach = bfs(atlantic_starts)

        return list(pacific_reach & atlantic_reach)


sol = Solution()

print(sol.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
print(sol.pacificAtlantic([[10, 10, 10], [10, 1, 10], [10, 10, 10]]))
print(sol.pacificAtlantic([[1]]))
