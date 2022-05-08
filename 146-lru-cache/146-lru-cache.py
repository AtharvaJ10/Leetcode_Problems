class Node:
    def __init__(self,key,value):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.d = dict()
        self.head = Node(0,0)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.delete(node)
            self.insert(node)
            return self.d[key].value
        return -1
    
    def delete(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def insert(self,node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            self.delete(node)
            self.insert(node)
            node.value = value
        else:
            if self.capacity<=len(self.d):
                self.deletetail()
            node = Node(key,value)
            self.insert(node)
            self.d[key] = node

    def deletetail(self):
        node = self.tail.prev
        del self.d[node.key]
        node.prev.next = self.tail
        self.tail.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)