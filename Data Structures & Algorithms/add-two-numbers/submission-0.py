# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        one = ten = 0

        while l1 and l2:
            sum = l1.val + l2.val + ten
            one = sum % 10
            cur.next = ListNode(val = one)
            cur = cur.next
            ten = sum // 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + ten
            one = sum % 10
            cur.next = ListNode(val = one)
            cur = cur.next
            ten = sum // 10
            l1 = l1.next

        while l2:
            sum = l2.val + ten
            one = sum % 10
            cur.next = ListNode(val = one)
            cur = cur.next
            ten = sum // 10
            l2 = l2.next

        if ten:
            cur.next = ListNode(val = ten)
            
        return dummy.next