from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeHelper:
    def buildTree(self, nodes):
        if not nodes:
            return None

        # The first element is the root
        root = TreeNode(nodes[0])
        queue = deque([root])
        i = 1

        while queue and i < len(nodes):
            current_node = queue.popleft()

            # Add left child
            if i < len(nodes) and nodes[i] is not None:
                current_node.left = TreeNode(nodes[i])
                queue.append(current_node.left)
            i += 1

            # Add right child
            if i < len(nodes) and nodes[i] is not None:
                current_node.right = TreeNode(nodes[i])
                queue.append(current_node.right)
            i += 1

        return root