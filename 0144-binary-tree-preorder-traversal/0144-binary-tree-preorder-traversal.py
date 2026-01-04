# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = [root]
        traversed_nodes = []

        if root is None:
            return traversed_nodes

        while nodes:
            node = nodes.pop()
            traversed_nodes.append(node.val)
            if node.right: nodes.append(node.right)
            if node.left : nodes.append(node.left)

        return traversed_nodes

        
        