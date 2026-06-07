# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def add(l1, l2, carry):
            if not l1 and not l2 and not carry:
                return None

            add1 = l1.val if l1 else 0
            add2 = l2.val if l2 else 0
            sum = add1 + add2 + carry
            cur = ListNode(val = sum % 10)
            cur.next = add(
                l1.next if l1 else None, 
                l2.next if l2 else None, 
                sum // 10
            )
            return cur

        return add(l1, l2, 0)