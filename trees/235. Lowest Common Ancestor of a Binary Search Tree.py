from treehelper import TreeNode, TreeHelper


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val > p.val and root.val < q.val:
            return root
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
            


sol = Solution()
th = TreeHelper()
root = th.buildTree([6,2,8,0,4,7,9,None,None,3,5]) # output should be 6 for p=2 q=8
rootp2, rootq8 = TreeNode(2), TreeNode(8)
r1 = th.buildTree([6,2,8,0,4,7,9,None,None,3,5]) # output should be 2 for p=2 q=4
r1p2, r1q4 = TreeNode(2), TreeNode(4)
r2 = th.buildTree([2,1]) # output should be 2 for p = 2 q = 1
r2p2, r2q1 = TreeNode(2), TreeNode(1)

print(sol.lowestCommonAncestor(root, rootp2, rootq8).val)
print(sol.lowestCommonAncestor(r1, r1p2, r1q4).val)
print(sol.lowestCommonAncestor(r2, r2p2, r2q1).val)
