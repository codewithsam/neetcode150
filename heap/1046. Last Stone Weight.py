import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq, -1*stone)
        while len(pq) > 1:
            s1 = -1 * heapq.heappop(pq)
            s2 = -1 * heapq.heappop(pq)
            res = abs(s1-s2)
            if res != 0:
                heapq.heappush(pq, -1*res)
        if len(pq) > 0:
            return -1*pq[0]
        else: return 0
        

sol = Solution()
print(sol.lastStoneWeight([2,7,4,1,8,1]))