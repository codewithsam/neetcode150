
from typing import Optional

from treehelper import TreeNode, TreeHelper

class Solution:
    def __init__(self):
        self.prev = float("-inf")

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        if not self.isValidBST(root.left): return False
        if root.val <= self.prev: return False
        self.prev = root.val
        return self.isValidBST(root.right)


th = TreeHelper()
sol1 = Solution()
sol2 = Solution()

root = th.buildTree([5,1,4,None,None,3,6])
root1 = th.buildTree([2,1,3])
print(sol1.isValidBST(root))
print(sol2.isValidBST(root1))
