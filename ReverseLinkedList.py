# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      """Something that I had to realize at first was that head was a pointer pointing to itself. From there we want to just iterate on the pointers,
      prev and curr are descriptive of the pointers. Create a holding variable next to hold the next pointer. Set curr.next equal to prev, prev equal to
      curr and curr equal to next. This makes sense since you want your pointer telling you where to go next to be reversed, so you set it equal to previous
      but you also need the next address which is why you create the nxt variable to store it while you overwrite the curr.next variable. Finally,
      you update the values of previous to your old current location and your new current to your old next (nxt variable). You return prev because at the end
      prev will contain the head of the reversed linkedlist and curr will contain head.next
      """
        prev = None
        curr = head
        while curr:
            nxt = curr.next 
            curr.next=prev
            prev = curr
            curr = nxt
        return prev
