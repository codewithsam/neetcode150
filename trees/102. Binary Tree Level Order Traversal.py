
from collections import deque
from typing import List, Optional

from treehelper import TreeNode, TreeHelper

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        result = []
        q.append(root)
        while q:
            subarr = []
            for _ in range(len(q)):
                root = q.popleft()
                subarr.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            result.append(subarr)
        return result

sol = Solution()
th = TreeHelper()
root = th.buildTree([1,2,3,4,5,6,7])
print(sol.levelOrder(root))