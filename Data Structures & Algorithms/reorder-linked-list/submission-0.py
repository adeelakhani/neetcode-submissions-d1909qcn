# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow=slow.next
        
        curr = slow.next
        prev = None
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev=curr
            curr=temp
        # so now prev is at head
        tmp2 = prev
        tmp = head
        while tmp and tmp2:
            firstNext = tmp.next
            secondNext = tmp2.next
            tmp.next = tmp2
            tmp2.next = firstNext
            tmp = firstNext
            tmp2 = secondNext





        # slow and fast pointer to find mid point
        # reverse the second list using algo
        # then start at 0 then take new pointer, start at head (0) then pts to n
        # then pts to 1 then pts to n-1(go through both and keep a copy of each of their nexts)