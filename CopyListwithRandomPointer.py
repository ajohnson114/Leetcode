"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
      """
      Make two passes. Once to make copies of all the nodes and the next to map all the pointers. In the first pass, we add all the current nodes to a 
      hash map and make all their values the copies we just created. In the second loop, we use the hash map we just created to query the copy nodes and
      set the pointers to what the original nodes would have them map to. This wouldn't work if we tried to create the copies and set the pointers all at 
      once because a node could have a pointer to a node that might not have been created so far. At the end of all this we can utilize our hash map once
      more and query it to find the copy that maps to the head (which was provided to us in the function call so we always have it).
      """
        oldtocopy = {None:None}
        
        curr = head
        
        while curr:
            copy = Node(curr.val)
            oldtocopy[curr] = copy
            curr = curr.next
        
        curr = head
        
        while curr:
            copy = oldtocopy[curr]
            copy.next = oldtocopy[curr.next]
            copy.random = oldtocopy[curr.random]
            curr = curr.next
        
        return oldtocopy[head]
