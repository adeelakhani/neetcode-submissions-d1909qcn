
class Node():
    def __init__(self, val=""):
        self.val = val
        self.next=None
        self.prev=None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head=Node()
        self.tail=Node()
        newNode = Node(homepage)
        self.head.next=newNode
        newNode.prev = self.head
        self.tail.prev=newNode
        newNode.next=self.tail
        self.currPos = newNode

    def visit(self, url: str) -> None:
        newNode=Node(url)
        self.currPos.next = newNode
        newNode.prev=self.currPos
        self.currPos = newNode
        self.tail.prev=self.currPos
        self.currPos.next=self.tail

    def back(self, steps: int) -> str:
        curr=self.currPos
        i = 0
        while curr is not self.head:
            self.currPos = curr
            if i == steps:
                return curr.val
            else:
                curr=curr.prev
                i+=1
        return self.currPos.val

    def forward(self, steps: int) -> str:
        curr=self.currPos
        i = 0
        while curr is not self.tail:
            self.currPos = curr
            if i == steps:
                return curr.val
            else:
                curr=curr.next
                i+=1
        return self.currPos.val



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)