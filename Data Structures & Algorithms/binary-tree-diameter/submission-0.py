# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        if not root:
            return 0

        left_d = self.maxDepth(root.left)
        right_d = self.maxDepth(root.right)
        depth = 1 + max(left_d, right_d)

        return depth


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_d = self.maxDepth(root.left)
        right_d = self.maxDepth(root.right)
        current_candidate = left_d + right_d
        left_candidate = self.diameterOfBinaryTree(root.left)
        right_candidate = self.diameterOfBinaryTree(root.right)

        return max(current_candidate, left_candidate, right_candidate)
