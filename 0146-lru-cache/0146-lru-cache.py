class Node():
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache ={}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        self.right.prev = node
        node.next = self.right
        
    def remove(self, node):
        prev, next  = node.prev, node.next
        prev.next, next.prev = next ,prev
        
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value  
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)