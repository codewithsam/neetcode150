from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        parent = [-1] * (n + 1)
        for u, v, w in times:
            adj[u].append((v, w))

        # Min-heap for Dijkstra (distance, node)
        pq = [(0, k)]
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for vertex, w in adj[node]:
                new_dist = d + w
                if new_dist < dist[vertex]:
                    dist[vertex] = new_dist
                    parent[vertex] = node
                    heapq.heappush(pq, (new_dist, vertex))

        max_dist = max(dist[1:])
        print(self.get_path(parent, n))
        return max_dist if max_dist < float("inf") else -1

    def get_path(self, parent, target):
        path = []
        while target != -1:
            path.append(target)
            target = parent[target]
        return path[::-1]  # take whole list and step in reverse order (-1)


sol = Solution()

print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # 2
print(sol.networkDelayTime([[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]], 4, 1))  # 3
print(sol.networkDelayTime([[1, 2, 1], [2, 3, 1]], 3, 2))  # -1
