
from typing import Optional

from treehelper import TreeNode, TreeHelper

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        prev,res = float("-inf"), None
        def _kthSmallest(root):
            nonlocal n, res, prev
            if not root: return True
            _kthSmallest(root.left)
            n+=1
            if n == k:
                res = root.val
                return
            _kthSmallest(root.right)
        _kthSmallest(root)
        return res
    
th = TreeHelper()
sol = Solution()
root = th.buildTree([3,1,4,None,2])
root1 = th.buildTree([5,3,6,2,4,None,None,1])


print(sol.kthSmallest(root, 1))
print(sol.kthSmallest(root1, 3))
