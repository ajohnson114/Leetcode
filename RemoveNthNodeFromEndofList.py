# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    This isn't so bad. Basically a preliminary idea would be to reverse the linked list and then remove the element and then rereverse it so that it's 
    in its original configuration. What you can do instead is iterate with two pointers and have the right pointer be n elements in front of the other and
    then remove the node that the left pointer is pointing to once the right pointer reaches the end of the linked list. What you'll find when you continue 
    in that logic is that you need the pointer of the previous element to successfully remove the pointer that the left one is pointing to. So what you 
    should do is make a dummy variable whose next element is the  head and then make the left pointer point to the dummy. You can rerun the same algorithm 
    as you did previous but only this time the right pointer will be n+1 elements in front of l (but you should still only iterate the right pointer n 
    times). Following this you set the next pointer of the element that the left pointer is at equal to the element after next aka skip one element and 
    set the next pointer to what the next pointer of the old next element used to be. Following this we want to return the head and the safest way to do
    this is to set it equal to what was after the dummy. This is better than returning the head because there are cases where the head was deleted and
    you'll get an error in those cases.
    """ 
        dummy = ListNode(0)
        dummy.next = head
        l,r = dummy, head
        
        while n > 0 and r:
            r = r.next
            n-=1
            
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        
        return dummy.next
