from typing import List
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for u, v, w in flights:
            adj[u].append((v, w))

        pq = []
        price = [float("inf")] * n

        heapq.heappush(pq, (0, src, 0))
        price[src] = 0

        while pq:
            stop, node, curr_price = heapq.heappop(pq)
            for v, p in adj[node]:
                newPrice = curr_price + p
                totalStop = stop + 1
                if totalStop <= k + 1:
                    if newPrice < price[v]:
                        price[v] = newPrice
                        heapq.heappush(pq, (stop + 1, v, newPrice))

        return price[dst]


sol = Solution()


# input array contains list with 3 values [from, to, price]

print(sol.findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))
print(sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
print(sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
print(sol.findCheapestPrice(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1))
print(sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
print(sol.findCheapestPrice(4, [[0, 1, 1], [1, 2, 1], [0, 2, 50], [2, 3, 1], [1, 3, 100]], 0, 3, 1))
