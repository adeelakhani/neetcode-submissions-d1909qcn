# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        fast = head
        slow = dummyNode
        for i in range(0, n):
            if fast:
                fast=fast.next
            else:
                break
        while fast:
            fast=fast.next
            slow = slow.next
        tmp = slow
        if slow.next:
            slow.next = tmp.next.next

        return dummyNode.next
        
            