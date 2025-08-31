import heapq
from typing import List
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for cords in points:
            d = (cords[0] ** 2) + (cords[1] ** 2)
            heapq.heappush(maxHeap, (-1*d, cords[0], cords[1]))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [[item[1], item[2]] for item in maxHeap]

sol = Solution()
print(sol.kClosest([[1,3],[-2,2]], 1))
print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))

        