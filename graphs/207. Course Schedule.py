from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        visited = [False for _ in range(numCourses)]
        pathvisited = [False for _ in range(numCourses)]

        def hasCycle(course):
            visited[course] = True
            pathvisited[course] = True
            if course in adj:
                for c in adj[course]:
                    if not visited[c]:
                        if hasCycle(c):
                            return True
                    elif pathvisited[c]:
                        return True
            pathvisited[course] = False
            return False

        for course in prerequisites:
            if course[1] not in adj:
                adj[course[1]] = []
            adj[course[1]].append(course[0])

        for course in range(0, numCourses):
            if not visited[course]:
                if hasCycle(course):
                    return False
        return True


sol = Solution()

# # Case 1: Large acyclic chain (possible to finish)
# print(sol.canFinish(10, [[i, i + 1] for i in range(9)]))
# # Expected: True (long linear chain, no cycle)

# # Case 2: Large cycle (impossible)
# print(sol.canFinish(10, [[i, (i + 1) % 10] for i in range(10)]))
# Expected: False (cycle across all 10 courses)

# Case 3: Multiple independent chains
print(sol.canFinish(9, [[0, 1], [1, 2], [2, 3], [4, 5], [0, 5], [5, 6], [6, 7], [8, 7]]))  # chain 1  # chain 2
# Expected: True (two separate chains, no cycle)

# Case 4: Multiple chains but with a cycle in one
print(sol.canFinish(8, [[0, 1], [1, 2], [2, 0], [4, 5], [5, 6], [6, 7]]))  # cycle in chain 1  # valid chain 2
# Expected: False

# # Case 5: Star dependency (all depend on one course)
# print(sol.canFinish(6, [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]))
# # Expected: True (all depend on course 0, no cycles)

# # Case 6: Star dependency with back edge (creates cycle)
# print(sol.canFinish(6, [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [0, 3]]))
# # Expected: False (0 → 3 → 0 cycle)

# # Case 7: Large sparse graph with no cycles
# print(sol.canFinish(1000, [[i, i + 1] for i in range(0, 999, 2)]))
# # Expected: True (only half of the chain connected, no cycle)

# # Case 8: Large dense graph with cycle
# edges = []
# for i in range(200):
#     for j in range(200):
#         if i != j:
#             edges.append([i, j])
# print(sol.canFinish(200, edges))
# # Expected: False (fully connected directed graph always has cycles)
