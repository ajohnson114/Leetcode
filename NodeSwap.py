def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
  """
  This is a bit of an annoying one conceptually. It's not hard but just annoying. So we create a dummy node to start and 
  set head as dummy.next. We also initialize curr as dummy. Then we loop through the linkedlist until curr.next.next and
  curr.next are invalid and we make the following changes. We set 2 pointers first and second to the next node and the 2nd 
  next node respectively. Then we say curr.next is second and first.next = second.next. Then we update second.next to 
  first and jump our curr pointer 2 nodes down to curr.next.next. It's strange but white board it out. At the end of this,
  we return dummy.next
  """
        if not head or not head.next: return head

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            curr.next = second
            first.next = second.next
            second.next = first
            curr = curr.next.next
        
        return dummy.next
