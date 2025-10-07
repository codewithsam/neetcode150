from DSU import DSU


class Solution:
    def kruskal(self, n, edges):
        dsu = DSU(n)
        weight = 0
        mst_edges = []

        edges.sort()

        for w, u, v in edges:
            if not dsu.connected(u, v):
                dsu.union(u, v)
                weight += w
                mst_edges.append((u, v, w))

        return weight, mst_edges


sol = Solution()
print(sol.kruskal(4, [(1, 0, 1), (3, 0, 2), (4, 0, 3), (2, 1, 2), (5, 1, 3), (7, 2, 3)]))
