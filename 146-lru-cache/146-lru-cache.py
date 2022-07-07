class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.size = capacity
        self.head = Node(0,0)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertHead(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.deleteNode(node)
            self.insertHead(node)
            return self.d[key].value
        return -1

    def deleteTail(self):
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        del self.d[node.key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            self.deleteNode(node)
            self.insertHead(node)
            node.value = value
        else:
            if self.size<=len(self.d):
                self.deleteTail()
            node = Node(key, value)
            self.insertHead(node)
            self.d[key] = node
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)