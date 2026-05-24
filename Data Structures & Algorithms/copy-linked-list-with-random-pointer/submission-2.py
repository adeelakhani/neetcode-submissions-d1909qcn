"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {}
        curr = head
        dummy = Node(0)
        tmp = dummy
        while curr:
            tmp.next = Node(curr.val)
            hashMap[curr] = tmp.next
            tmp = tmp.next
            curr = curr.next
        curr = head
        while curr:
            dNode = hashMap[curr]
            randomVal = hashMap[curr.random] if curr.random else None
            dNode.random = randomVal
            curr = curr.next
        return dummy.next



              