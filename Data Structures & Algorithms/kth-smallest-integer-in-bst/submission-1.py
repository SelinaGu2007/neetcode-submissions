# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countChildren(self, root):
        if not root:
            return 0, 0

        if root.left:
            left_count = self.countChildren(root.left)[0] + self.countChildren(root.left)[1] + 1
        else:
            left_count = 0

        if root.right:
            right_count = self.countChildren(root.right)[0] + self.countChildren(root.right)[1] + 1
        else:
            right_count = 0

        return left_count, right_count

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        left, right = self.countChildren(root)

        if k <= left:
            return self.kthSmallest(root.left, k)
        if k == left + 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k - left - 1)
