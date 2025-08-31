from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskcounter = Counter(tasks)
        q = deque()
        maxHeap = [-1*taskcounter[key] for key in taskcounter]
        heapq.heapify(maxHeap)
        timer = 0
        while maxHeap or q:
            timer+=1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append((count, timer+n))
            if q and q[0][1] == timer:
                heapq.heappush(maxHeap, q.popleft()[0])
        return timer

            

sol = Solution()
print(sol.leastInterval(["A","A","A","B","C"], 3))