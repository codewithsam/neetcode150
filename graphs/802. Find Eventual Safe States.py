from collections import deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(len(graph))}
        outdegree = [0] * len(graph)
        toposort = []
        res = []

        for i, nodes in enumerate(graph):
            for node in nodes:
                adj[node].append(i)
                outdegree[i] += 1

        q = deque()

        for i in range(len(outdegree)):
            if outdegree[i] == 0:
                q.append(i)

        while q:
            v = q.popleft()
            toposort.append(v)
            for n in adj[v]:
                outdegree[n] -= 1
                if outdegree[n] == 0:
                    q.append(n)

        for i in range(len(outdegree)):
            if outdegree[i] == 0:
                res.append(i)

        return res


sol = Solution()
print(sol.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
