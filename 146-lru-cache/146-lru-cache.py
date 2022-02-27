class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.d = dict()
        self.head = Node(0,0)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.deletekey(node)
            self.inserthead(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            self.deletekey(node)
            self.inserthead(node)
            node.value = value
        else:
            if len(self.d)>=self.size:
                self.deletetail()
            node = Node(key,value)
            self.d[key] = node
            self.inserthead(node)
    
    
    def deletekey(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def inserthead(self,node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        
    def deletetail(self):
        temp = self.tail.prev
        del self.d[temp.key]
        temp.prev.next = self.tail
        self.tail.prev = temp.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)