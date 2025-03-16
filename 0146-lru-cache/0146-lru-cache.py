class Node:
    def __init__(self,key,val):
        self.val=val
        self.key=key
        self.prev=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        self.cache={}

    def insert(self,node):
        nxt=self.right
        prv=self.right.prev

        node.next=nxt
        node.prev=prv

        prv.next=node
        self.right.prev=node
  
    def remove(self,node):
        prv=node.prev
        nxt=node.next

        prv.next=nxt
        nxt.prev=prv

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else: return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)