from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i: [] for i in range(1, n + 1)}
        visited = [False] * (n + 1)
        cycle_nodes = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def findCycleNode(v, parent):
            visited[v] = True

            for n in adj[v]:
                if not visited:
                    if findCycleNode(n, v):
                        return True
                elif n != parent:
                    cycle_nodes.add((n, v))
                    return True
            return False

        for v in range(1, n + 1):
            if not visited[v]:
                findCycleNode(v, -1)
        print(cycle_nodes)


sol = Solution()
print(sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
print(sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
