class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 1
        self.next = self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def append(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node
        self.size+=1
        
    def pop(self, node = None):
        if self.size==0:
            return
        if not node:
            node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size-=1
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.d = defaultdict()
        self.freq = defaultdict(DoublyLinkedList)
        self.min_freq = 0
    
    def update(self, node):
        freq = node.freq
        self.freq[freq].pop(node)
        if self.min_freq == freq and len(self.freq[freq])==0:
            self.min_freq+=1
        node.freq+=1
        self.freq[node.freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.size==0:
            return
        if key in self.d:
            node = self.d[key]
            self.update(node)
            node.val = value
        else:
            print(self.size)
            if self.size<=len(self.d):
                node = self.freq[self.min_freq].pop()
                del self.d[node.key]
            node = Node(key, value)
            self.freq[1].append(node)
            self.d[node.key] = node
            self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)