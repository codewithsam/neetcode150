from typing import Optional

from treehelper import TreeNode, TreeHelper


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        height = 0

        def _maxHeight(root):
            nonlocal height
            if root == None:
                return 0
            lh = _maxHeight(root.left)
            rh = _maxHeight(root.right)
            height = max(height, lh + rh)
            return 1 + max(lh, rh)

        _maxHeight(root)
        return height


sol = Solution()
th = TreeHelper()
tree = th.buildTree([1, 2, None, 3, None, 4])
tree2 = th.buildTree([1, None, 2, 3, 4, 5, None])

# print(sol.diameterOfBinaryTree(tree))
print(sol.diameterOfBinaryTree(tree2))
