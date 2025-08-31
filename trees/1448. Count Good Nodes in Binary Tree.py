

from treehelper import TreeNode, TreeHelper


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = 0
        maximum = float("-inf")
        def _goodNodes(root, maximum):
            nonlocal output
            if not root:
                return
            if root.val >= maximum:
                output+=1
                maximum = root.val
            _goodNodes(root.left, maximum)
            _goodNodes(root.right, maximum)
        _goodNodes(root, maximum)
        return output

sol = Solution()
th = TreeHelper()
root = th.buildTree([3,1,4,3,None,1,5]) # answer should be 4
print(sol.goodNodes(root))