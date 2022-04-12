# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      """
      This is a linkedlist problem. To avoid any edge cases, we start off with a dummy node that will take care of cases when we have an empty list given
      to us or something like that. Then while both lists are not None we do the two finger method and if one is smaller than the other we add it to the 
      output list and then iterate it. After we do that once we need to move our pointer one index forward to the most recent node we just added. 
      We do that until one of the list (or both) no longer exists. Following this we need to check if one of the lists exists and if it does we just need
      to add that linkedlist to the end of the list and then we just return what was after our dummy node.
      """
        dummy = ListNode()
        tail=dummy
        
        while list1 and list2 :
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next=list1
        elif list2:
            tail.next=list2
            
        return dummy.next
        
