# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        # given 1 -> 2 -> 3 -> 4
        # head is on 1, we wanna flip the poitner
        # save head.next to temp, then flip the curr.next to point to the prev which is None
        # then prev to come to curr and curr to go next via going to where temp is