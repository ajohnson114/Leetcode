# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      """
      Floyd's cycle detection algorithm. Start 2 pointers at the start of the linked list and have one be the slow pointer that gets iterated once
      and the other be the fast one which gets iterated twice on each go. While fast and fast.next exist we know that we haven't reached the end of the list
      and Floyd's algorithm says that when these two pointers meet we will be at the start of the cycle in the linked list. Therefore I put a boolean for 
      if we found it or not and then just set it to True if we found it and set it's default equal to false and returned the boolean at the end.
      """
        slow, fast = head, head
        
        found = False
        
        while 1 and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                found = True
                break
                
        return found
            
