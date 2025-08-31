

from collections import deque
from typing import List, Optional

from treehelper import TreeNode, TreeHelper


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque()
        q.append(root)
        result = []
        while q:
            queueSize = len(q)
            for i in range(1,queueSize+1):
                root = q.popleft()
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
                if i == queueSize:
                    result.append(root.val)
        return result
    
sol = Solution()
th = TreeHelper()
root = th.buildTree([1,2,3,None,5,None,4])
root1 = th.buildTree([1,2,3,4,None,None,None,5])
root2 = th.buildTree([1,None,3])

print(sol.rightSideView(root))
print(sol.rightSideView(root1))
print(sol.rightSideView(root2))


