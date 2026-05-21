# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# list: Optional[ListNode], says list is a object of ListNode
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = list1
        curr2 = list2
        newList = ListNode()
        head = newList
        while curr or curr2:
            if not curr:
                newList.next = curr2
                break
            elif not curr2:
                newList.next = curr
                break
            else:
                if curr.val > curr2.val:
                    newList.next = curr2
                    curr2=curr2.next
                    newList = newList.next
                else:
                    newList.next = curr
                    curr=curr.next
                    newList = newList.next
        return head.next



