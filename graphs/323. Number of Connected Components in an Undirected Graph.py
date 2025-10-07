from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        visited = [False] * n
        count = 0

        def dfs(v):
            visited[v] = True
            for n in adj[v]:
                if not visited[n]:
                    dfs(n)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for v in adj:
            if not visited[v]:
                count += 1
                dfs(v)
        return count


sol = Solution()
print(sol.countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]))
