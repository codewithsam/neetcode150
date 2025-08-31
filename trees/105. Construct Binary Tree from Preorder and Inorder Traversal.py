
from typing import List, Optional

from treehelper import TreeNode, TreeHelper


class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def _buildTree(preorder, inorder):
            if len(inorder) <= 0: return None
            nodeval = preorder.pop(0)
            root = TreeNode(nodeval)
            splitidx = inorder.index(nodeval)
            left = inorder[:splitidx]
            right = inorder[splitidx+1:]

            root.left = _buildTree(preorder, left)
            root.right = _buildTree(preorder, right)
            return root
        return _buildTree(preorder, inorder)


sol = Solution()
th = TreeHelper()
root = th.buildTree([10,5,15,2,7,12,20,1,3,6,8,13,18,25])
head = sol.buildTree([10, 5, 2, 1, 3, 7, 6, 8, 15, 12, 13, 20, 18, 25], [1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 18, 20, 25])

    #           10
    #        /      \
    #      5          15
    #    /   \      /    \
    #   2     7    12     20
    #  / \   / \     \   /  \
    # 1   3 6   8    13 18  25