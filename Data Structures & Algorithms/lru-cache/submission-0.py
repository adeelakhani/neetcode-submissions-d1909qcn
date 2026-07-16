class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1,0)
        self.tail = Node(-1,0)
        self.head.prev, self.tail.next = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            print("node:", node.key, "node.prev:", node.prev, "node.next:", node.next)
            node.prev.next, node.next.prev = node.next, node.prev
            self.head.prev.next, node.prev = node, self.head.prev
            node.next = self.head
            self.head.prev = node
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity:
            lru = self.tail.next
            self.tail.next, lru.next.prev = lru.next, self.tail
            # no need to delete since the garbage collector will clean it up
            del self.cache[lru.key]
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.prev.next, node.next.prev = node.next, node.prev
        else:
            self.cache[key] = Node(key, value)
        node = self.cache[key]
        self.head.prev.next = node
        node.prev = self.head.prev
        node.next = self.head
        self.head.prev = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)