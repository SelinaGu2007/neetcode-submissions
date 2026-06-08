# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(root):
            if not root:
                return 0

            left_d = depth(root.left)
            right_d = depth(root.right)
            return 1 + max(left_d, right_d)

        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False

        left = depth(root.left)
        right = depth(root.right)

        return abs(left - right) <= 1