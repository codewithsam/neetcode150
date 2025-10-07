from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        indegree = [0 for _ in range(numCourses)]
        q = deque()
        toposort = []

        for course in prerequisites:
            if course[1] not in adj:
                adj[course[1]] = []
            adj[course[1]].append(course[0])
            indegree[course[0]] += 1

        for i, c in enumerate(indegree):
            if c == 0:
                q.append(i)

        while q:
            c = q.popleft()
            toposort.append(c)
            if c in adj:
                for v in adj[c]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)

        return toposort if len(toposort) == len(indegree) else []


sol = Solution()

# Case 6: Larger graph, no cycles
print(sol.findOrder(6, [[1, 0], [2, 1], [3, 2], [4, 2], [5, 3], [5, 4]]))
# Expected: [0,1,2,3,4,5] (unique order)

# Case 1: Simple chain (unique order)
print(sol.findOrder(4, [[1, 0], [2, 1], [3, 2]]))
# Expected: [0,1,2,3]

# Case 2: Multiple valid orders
print(sol.findOrder(2, [[1, 0]]))
# Expected: [0,1] (only one valid order)

# Case 3: Disconnected graph (independent chains)
print(sol.findOrder(4, [[1, 0], [3, 2]]))
# Expected: [0,1,2,3] or [2,3,0,1] (any valid order is fine)

# Case 4: Cycle → impossible
print(sol.findOrder(2, [[0, 1], [1, 0]]))
# Expected: [] (empty list, because no valid ordering)

# Case 5: Star dependency (one root course)
print(sol.findOrder(4, [[1, 0], [2, 0], [3, 0]]))
# Expected: [0,1,2,3] or [0,2,1,3] etc. (0 must come first)

# Case 7: Larger graph with a cycle
print(sol.findOrder(6, [[1, 0], [2, 1], [3, 2], [1, 3], [4, 2], [5, 4]]))
# Expected: [] (cycle 1→2→3→1 prevents ordering)

# Case 8: No prerequisites
print(sol.findOrder(3, []))
# Expected: [0,1,2] or any permutation (since all are independent)

# Case 9: All courses dependent on single course
print(sol.findOrder(5, [[1, 0], [2, 0], [3, 0], [4, 0]]))
# Expected: [0,1,2,3,4] (0 must be before all others)

# Case 10: Multiple independent chains that merge
print(sol.findOrder(5, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]))
# Expected: [0,1,2,3,4] or [0,2,1,3,4] (0 first, then 1 and 2, then 3, then 4)
