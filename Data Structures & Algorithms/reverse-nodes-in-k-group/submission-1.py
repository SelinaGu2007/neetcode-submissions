# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        num = 0
        while cur:
            num += 1
            if num == k:
                break
            cur = cur.next

        if num < k:
            return head

        prev = self.reverseKGroup(cur.next, k)
        cur.next = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev

        