from collections import deque
from typing import List
import heapq


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for w in words for c in w}
        q = deque()
        toposort = []

        for i in range(0, len(words) - 1):
            str1 = words[i]
            str2 = words[i + 1]
            minlen = min(len(str1), len(str2))
            if len(str1) > len(str2) and str1[:minlen] == str2[:minlen]:  # if str2 is a prefix of str1
                return ""
            for j in range(0, min(len(str1), len(str2))):
                if str1[j] != str2[j]:
                    adj[str1[j]].add(str2[j])
                    break

        for k, v in adj.items():
            for item in v:
                indegree[item] += 1

        for k, v in indegree.items():
            if v == 0:
                q.append(k)

        while q:
            v = q.popleft()
            toposort.append(v)
            if v in adj and len(adj[v]) > 0:
                for n in adj[v]:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        q.append(n)

        return "".join(toposort) if len(toposort) == len(adj) else ""


############### IF THE QUESTION ASKS FOR LEXICOGRAPHICALLY CORRECT AND DETERMINISTIC POP USE HEAQ SOLUTION ############


class Solution2:
    def alienOrder(self, words):
        if not words:
            return ""

        # Step 1: Build adjacency list & indegree map
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for w in words for c in w}

        # Step 2: Build graph edges
        for i in range(len(words) - 1):
            str1, str2 = words[i], words[i + 1]
            minlen = min(len(str1), len(str2))

            # Invalid prefix case: "abc" before "ab"
            if len(str1) > len(str2) and str1[:minlen] == str2[:minlen]:
                return ""

            for j in range(minlen):
                if str1[j] != str2[j]:
                    if str2[j] not in adj[str1[j]]:
                        adj[str1[j]].add(str2[j])
                        indegree[str2[j]] += 1
                    break

        # Step 3: Initialize min-heap with indegree = 0
        heap = [c for c in indegree if indegree[c] == 0]
        heapq.heapify(heap)

        toposort = []

        # Step 4: Kahn's Algorithm with min-heap
        while heap:
            v = heapq.heappop(heap)
            toposort.append(v)
            for n in adj[v]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    heapq.heappush(heap, n)

        # Step 5: Cycle check
        return "".join(toposort) if len(toposort) == len(adj) else ""


sol = Solution()
# ✅ Basic case from your example
print(sol.foreignDictionary(["hrn", "hrf", "er", "enn", "rfnn"]))
# Expected: "hernf" (or equivalent valid order)

# ✅ Prefix rule violation
print(sol.foreignDictionary(["abc", "ab"]))
# Expected: "" (invalid)

# ✅ Multiple valid orders
print(sol.foreignDictionary(["ab", "ac"]))
# Expected: could be "bac" or "abc" depending on implementation

# ✅ Disconnected graph
print(sol.foreignDictionary(["x", "y", "z"]))
# Expected: "xyz" or any permutation of "x","y","z"

# ✅ Cycle detection
print(sol.foreignDictionary(["za", "zb", "ca", "cb"]))
# Expected: "" (invalid)

# ✅ Single word
print(sol.foreignDictionary(["hello"]))
# Expected: "helo" or any order of unique chars

# ✅ Characters with no constraints
print(sol.foreignDictionary(["wrt", "wrf", "er", "ett", "rftt"]))
# Expected: "wertf" (classic test case)
