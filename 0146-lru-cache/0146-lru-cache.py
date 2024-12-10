class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.prev,self.next=None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
    
    def remove(self,node):
        prev=node.prev
        nxt=node.next

        prev.next=nxt
        nxt.prev=prev
    
    def insert(self,node):
        prev=self.right.prev
        nxt=self.right

        node.prev=prev
        node.next=nxt

        nxt.prev=node
        prev.next=node     

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

# Time Complexity - O(1) for each put and get operation
# Space complexity - O(n)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)