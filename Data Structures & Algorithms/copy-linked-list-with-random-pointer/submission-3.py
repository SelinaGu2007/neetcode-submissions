"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        cur2 = head
        while cur2:
            if cur2.next:
                old_to_new[cur2].next = old_to_new[cur2.next]
            if cur2.random:
                old_to_new[cur2].random = old_to_new[cur2.random]
            cur2 = cur2.next

        if head:
            return old_to_new[head]

        return None