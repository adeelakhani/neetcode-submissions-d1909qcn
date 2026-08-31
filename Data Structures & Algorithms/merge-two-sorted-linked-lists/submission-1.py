# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# list: Optional[ListNode], says list is a object of ListNode
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        head = merged
        p1 = list1
        p2 = list2

        while True:
            if not p1:
                merged.next=p2
                break
            elif not p2:
                merged.next = p1
                break
            else:
                if p1.val <= p2.val:
                    merged.next = p1
                    merged = merged.next
                    p1=p1.next
                else:
                    merged.next = p2
                    merged = merged.next
                    p2=p2.next
        return head.next


