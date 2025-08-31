import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]
    

kth = KthLargest(3, [1, 2, 3, 3])
print(kth.add(3))
print(kth.add(5))
print(kth.add(6))
print(kth.add(7))
print(kth.add(8))

# kth2 = KthLargest(4, [4, 5, 5, 6, 6, 7])
# print(kth2.add(7))
# print(kth2.add(8))
# print(kth2.add(5))
# print(kth2.add(6))