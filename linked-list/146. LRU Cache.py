class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev, self.next = None, None

class LinkedList:
    def __init__(self):
        self.head = Node(-1,-1) # all least recently used nodes will be on the left side tied to head
        self.tail = Node(-1,-1) # all most recently used nodes will be on the right side tied to tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, newNode):
        oldnode = self.tail.prev
        oldnode.next = newNode
        newNode.prev = oldnode
        newNode.next = self.tail
        self.tail.prev = newNode

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def removeLRU(self):
        lrunode = self.head.next
        lrukey = self.head.next.key
        self.head.next = lrunode.next
        lrunode.next.prev = self.head
        return lrukey

class LRUCache:

    def __init__(self, capacity: int):
        self.linked_list = LinkedList()
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.linked_list.remove(self.cache[key])
            self.linked_list.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.linked_list.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.linked_list.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lrukey = self.linked_list.removeLRU()
            del self.cache[lrukey]



lru = LRUCache(2)
lru.put(1,1)
lru.put(2,2)
print(lru.get(1))
lru.put(3,3)
print(lru.get(2))
lru.put(4,4)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))

