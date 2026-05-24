# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases, 1 linkedlist longer than the other
        # same length but theres a carry

        dummy = ListNode(0)
        dc = dummy
        curr1 = l1
        curr2 = l2
        carry = 0
        while curr1 or curr2 or carry != 0:
            total = 0
            if curr1 and not curr2:
                total = (curr1.val + 0 + carry) % 10
                carry = curr1.val + carry
            elif curr2 and not curr1:
                total = (curr2.val + 0 + carry) % 10
                carry = curr2.val + carry
            elif not curr2 and not curr1:
                total = carry
                carry = 0
            else:
                total = (curr1.val + curr2.val + carry) % 10
                carry = (curr1.val + curr2.val + carry) // 10
            dc.next = ListNode(total)
            dc = dc.next
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next
        return dummy.next




