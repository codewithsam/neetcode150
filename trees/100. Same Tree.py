from typing import Optional

from treehelper import TreeNode, TreeHelper


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

sol = Solution()
treehelper = TreeHelper()
p = treehelper.buildTree([1,2,3])
q = treehelper.buildTree([1, None,3])
print(sol.isSameTree(p,q))

p1 = treehelper.buildTree([1,2,3])
q1 = treehelper.buildTree([1, 2,3])
print(sol.isSameTree(p1,q1))