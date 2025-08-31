from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        seen = {}
        time = 0
        for task in tasks:
            if task in seen and seen[task] > time:
                time = seen[task]
            seen[task] = time+space+1
            time+=1
        return time





sol = Solution()
print(sol.taskSchedulerII([1,2,1,2,3,1], 3))
print(sol.taskSchedulerII([5,8,8,5], 2))