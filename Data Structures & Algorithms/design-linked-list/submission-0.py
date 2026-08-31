class Node:
    def __init__(self, val=0):
        self.val=val
        self.next=None
        self.prev=None
class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next=self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            curr=curr.next
            i+=1
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next.prev=newNode
        self.head.next = newNode
        newNode.prev = self.head

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        newNode.prev = self.tail.prev
        self.tail.prev.next=newNode
        newNode.next=self.tail
        self.tail.prev=newNode

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                if curr == self.head.next:
                    addAtHead(val)
                    break
                elif curr == self.tail:
                    addAtTail(val)
                    break
                else:
                    newNode = Node(val)
                    temp = curr.prev
                    temp.next=newNode
                    newNode.prev=temp
                    newNode.next = curr
                    curr.prev=newNode
                    break
            curr=curr.next
            i+=1


    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                if curr == self.tail:
                    break
                else:
                    temp = curr.prev
                    temp.next=curr.next
                    curr.next.prev=temp
                    break
            curr=curr.next
            i+=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)