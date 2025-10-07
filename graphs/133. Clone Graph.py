# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        seen = {}

        def _dfs(node):
            if not node:
                return None
            if node in seen:
                return seen[node]
            newnode = Node(node.val)
            seen[node] = newnode
            for vertex in node.neighbors:
                newnode.neighbors.append(_dfs(vertex))
            return newnode

        return _dfs(node)
