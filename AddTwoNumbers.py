# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      """
      Bit of an annoying question. Basically it is adding two numbers but you need to remember to add the carry on digit at all points in time. So per usual
      with linked list questions, we start with a dummy node and initialize our current variable to it as well as having a preset value for carry.
      We iterate while there are still numbers in l1 or l2 or carry (carry is included in the condition because of the case of 7+8 both lists will run out
      but there will still be a carry and new node that needs to get added. To begin, the loop we say that if there is a value make it our variable and
      if there isn't a value make it 0 and then add it plus the carry we just computed. The carry will be the 10's position of our sum and the value we want
      is the ones both of which can be got pretty simply. Therefore, we set the next node equal to the value found and update our current pointer and then
      we update l1 and l2 if they exist or make them none. Finally we return dummy.next aka the head of the result.
      """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val %= 10
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        
        return dummy.next
