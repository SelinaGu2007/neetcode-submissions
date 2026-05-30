# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = []
        cur = head
        while cur:
            l.append(cur)
            cur = cur.next

        for i in range(len(l) // 2):
            l[i].next = l[len(l) - 1 - i]
            l[len(l) - 1 - i].next = l[i+1]
        l[len(l) // 2].next = None
