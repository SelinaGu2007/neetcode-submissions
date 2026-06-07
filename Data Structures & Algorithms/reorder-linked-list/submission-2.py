# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = slow
        cur = slow.next
        slow.next = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        while prev.next:
            next_head = head.next
            next_prev = prev.next

            tmp = head.next
            head.next = prev
            prev.next = tmp
            prev = next_prev
            head = next_head
