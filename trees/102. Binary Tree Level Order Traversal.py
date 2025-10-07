from collections import deque
from typing import List, Optional

from treehelper import TreeNode, TreeHelper


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        result = []
        q.append(root)
        while q:
            node = q.popleft()
            result.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print([r.val for r in result])
        return result


sol = Solution()
th = TreeHelper()
root = th.buildTree([1, 2, 3, 4, 5, 6, 7])
print(sol.levelOrder(root))
