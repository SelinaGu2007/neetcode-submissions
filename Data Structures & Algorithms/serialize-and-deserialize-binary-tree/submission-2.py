# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                res.append("#")
                continue
            
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "#":
            return None

        root = TreeNode(val = vals[0])
        queue = deque([root])

        i = 0
        while queue:
            node = queue.popleft()

            i += 1
            if vals[i] != "#":
                node.left = TreeNode(val = vals[i])
                queue.append(node.left)

            i += 1
            if vals[i] != "#":
                node.right = TreeNode(val = vals[i])
                queue.append(node.right)

        return root
        
