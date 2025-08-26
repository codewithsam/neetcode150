from typing import Optional
from treehelper import TreeNode, TreeHelper

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: return root
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            temp = node.right
            node.right = node.left
            node.left = temp
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root
    
sol = Solution()
root = TreeHelper.buildTree([4,2,7,1,3,6,9])
r = sol.invertTree(root)
