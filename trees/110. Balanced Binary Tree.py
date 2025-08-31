from typing import Optional

from treehelper import TreeNode, TreeHelper


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isGood = True
        def _isBalanced(root):
            nonlocal isGood
            if root is None or isGood is False:
                return 0
            lh = 1+ _isBalanced(root.left)
            rh = 1+ _isBalanced(root.right)
            if abs(lh-rh) > 1:
                isGood = False
            return max(lh,rh)
        _isBalanced(root)
        return isGood
    
sol = Solution()
th = TreeHelper()
root = th.buildTree([3,9,20,None,None,15,7])
print(sol.isBalanced(root))
root1 = th.buildTree([1,2,2,3,3,None,None,4,4])
print(sol.isBalanced(root1))