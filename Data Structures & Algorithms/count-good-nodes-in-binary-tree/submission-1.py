# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque([(root, float("-inf"))])

        num = 0
        while queue:
            n = len(queue)

            for i in range(n):
                node, max_val = queue.popleft()
                if not node:
                    continue

                if node.val >= max_val:
                    num += 1
                    max_val = node.val

                queue.append((node.left, max_val))
                queue.append((node.right, max_val))

        return num