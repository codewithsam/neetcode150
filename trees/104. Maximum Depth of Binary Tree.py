from typing import Optional

from treehelper import TreeNode, TreeHelper

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        return 1 + max( self.maxDepth(root.left), self.maxDepth(root.right))

sol = Solution()
tree = TreeHelper.buildTree([3,9,20,None,None,15,7])
print(sol.maxDepth(tree))