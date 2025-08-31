
from typing import Optional

from treehelper import TreeNode, TreeHelper


class Solution:
    def isSameTree(self, p: Optional[TreeNode],q: Optional[TreeNode]):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True   # Empty tree is always a subtree
        if not root:
            return False  # Can't match if root is exhausted

        if self.isSameTree(root, subRoot):
            return True
        
        # Keep searching in left or right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    

sol = Solution()

th = TreeHelper()
root = th.buildTree([3,4,5,1,2])
subRoot = th.buildTree([4,1,2])
print(sol.isSubtree(root, subRoot))
r = [3,4,5,1,2,None,None,None,None,0]
s = [4,1,2]
r1 = th.buildTree(r)
s1 = th.buildTree(s)
print(sol.isSubtree(r1,s1))