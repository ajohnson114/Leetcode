"""
For this question you want to do two things. You want a doubly linked list where the left most pointer is the least recently used value and the right is 
the most recently used value. Furthermore, you want a dictionary where the key is the key of the input and the value is a node in the doubly linked list.
So we create a new class Node which is to be our node in our doubly linked list. It will take in a key and a value and instantiate two pointers as prev 
and next (both being none at the start). Then we move on to our original implementation. Knowing that we're going for a doubly linked list implementation
we'll find that it's useful for us to add two helpful functions for linked list operations, the two are: remove and insert. Remove removes from the linked
list and insert will add the node to the right of the linked list. Remove removes the node from the list by saying the node in front of the node we're 
trying to remove points to the node behind the node we want to remove and the node behind the node we want to remove points to the one in front of it. 
Insert inserts by getting the node behind the right most node and the right most node and saying that they both respectively point to the new node we're
inserting. Finally we adjust the node we're currently at to say that it's next node is the right most node and the node behind it is the previous node. 
From here things get a lot simpler. For our initialization, we save our capacity, create a dictinary to map the keys to the nodes and say that at first our
left and right pointers point to dummy node and set pointers for both those nodes. From there get can be created by saying that if the key is in our 
dictionary, then we should call our remove function on it and then reinsert it into our linked list since we have a new most recently used key, otherwise
return -1. Finally for our put function, we want to remove our value if it's in our dictionary and then create a enw node with the key and value and then
reinsert it. Then we want to check if we have more values than our capacity. If we do we want to delete from the left by calling lru = self.left.next 
(our first node on the left is a dummy node) then calling our remove function and then deleting the value we found from our hashmap. All of this completes
our answer
"""
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev, self.next = None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # maps key to node
        self.left,self.right = Node(0,0),Node(0,0)
        #self.left = least recently used, self.right = most recent
        self.left.next, self.right.prev = self.right,self.left
        
    def remove(self,node): #remove from list
        nxt, prev = node.next, node.prev
        nxt.prev, prev.next = prev, nxt
        
    def insert(self,node): #insert at right
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev= nxt,prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            #remove from linked list and delete from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
