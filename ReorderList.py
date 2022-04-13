# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    """  
    This one isn't so bad. Basically you want to split the list in half so to speak. If the list is odd then the second half of the list is the one with 
    n/2 - 1 elements. You can figure out where the middle of the list is by setting two pointers at the first and second elements in the list and then 
    moving the slow pointer once and the second pointer twice. When the second, fast pointer reaches the last element or a null element. The next element 
    in the linked list for the slow pointer will be half way through the list. (When the fast pointer moves n elements the slow pointer will move n/2)
    One way to make sure we don't overshoot is to make sure that we always have the fast pointer and the next element after that is valid if the next 
    element is null we know we're at the end of the list. From there we have both halves of the list. After that we want to reverse the second half of the 
    list. Quick linked list reversing refresh is: start with a null ptr as prev set a current variable and then set next equal to some temporary value
    set the next pointer equal to prev and then move on to the next iteration by making the next prev equal to your current value and updating your current
    value with the place holder next value. Following that we merge the lists by having 2 place holder values to hold the next pointer, setting the element 
    in the first half of the list equal to the first element in the now reversed second half list setting the pointer from the first element in the second
    list equal to what use to be the second element in the first half of the list and then updating to move on to the next iteration.  
    
    """  
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next #second half of list
        prev = slow.next = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #merge two halfs
        first, second = head, prev
        
        while second:
            tmp1, tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            
        
