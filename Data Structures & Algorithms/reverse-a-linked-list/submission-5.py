# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recurse(curr, prev):
            if not curr:
                return prev
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            return recurse(temp, prev)
        return recurse(head, None)

        
        # have temp point to the next
        # hit the switcheroo
        # go to the next