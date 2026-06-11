# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = [[root.val]]

        queue = deque([root])
        num = 1
        while queue:
            cur_layer = []
            for i in range(num):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    cur_layer.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    cur_layer.append(node.right.val)

            if cur_layer:
                res.append(cur_layer)
            num = len(cur_layer)

        return res
            