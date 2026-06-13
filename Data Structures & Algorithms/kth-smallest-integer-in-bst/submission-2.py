# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count_child = {}

        def countChildren(root):
            if not root:
                return 0

            left_count = countChildren(root.left)

            right_count = countChildren(root.right)

            count_child[root] = (left_count, right_count)

            return left_count + right_count + 1

        countChildren(root)
        left, right = count_child[root]

        if k <= left:
            return self.kthSmallest(root.left, k)
        if k == left + 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k - left - 1)
