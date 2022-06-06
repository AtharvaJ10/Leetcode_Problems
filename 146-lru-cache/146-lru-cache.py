class Node:
    def __init__(self,key,value):
        self.next = None
        self.prev = None
        self.value = value
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.d = dict()
        self.head = Node(0,0)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.delete(node)
            self.insert(node)
            return node.value
        else:
            return -1
        
    def delete(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self,node):
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            self.delete(node)
            self.insert(node)
            node.value = value
        else:
            if len(self.d)>=self.size:
                del self.d[self.tail.prev.key]
                self.deletetail()
            node = Node(key,value)
            self.d[key] = node
            self.insert(node)
    
    def deletetail(self):
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)