class Solution:
    def valid_tree(self, n, edges):
        # write your code here
        adj = {i: [] for i in range(n)}
        visited = [False] * n

        def hasCycle(v, parent):
            visited[v] = True
            for n in adj[v]:
                if not visited[n]:
                    if hasCycle(n, v):
                        return True
                elif n != parent:
                    return True
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        if hasCycle(0, -1):
            return False

        return all(visited)


sol = Solution()
print(sol.valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(sol.valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
