# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False

            if not isSameTree(p.left, q.left):
                return False
            if not isSameTree(p.right, q.right):
                return False

            return p.val == q.val
        
        def maxDepth(root: Optional[TreeNode]) -> int:
            depth = 0

            if not root:
                return 0

            left_d = maxDepth(root.left)
            right_d = maxDepth(root.right)
            depth = 1 + max(left_d, right_d)

            return depth

        root_d = maxDepth(root)
        subRoot_d = maxDepth(subRoot)

        depth = root_d - subRoot_d
        if depth < 0:
            return False
        if depth == 0:
            return isSameTree(root, subRoot)

        queue = [root]
        for i in range(depth):
            n = len(queue)
            for j in range(n):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        for node in queue:
            if isSameTree(node, subRoot):
                return True

        return False