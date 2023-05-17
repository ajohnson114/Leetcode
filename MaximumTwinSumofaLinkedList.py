
  def pairSum(self, head: Optional[ListNode]) -> int:
    """
    ll = [1,2,3,4] reverse_mid -> [1,2,4,3] process -> 1+4, 2+3 etc. The biggest sum is the answer which is 5
    The premise of this is to find the middle of the list, reverse it and then add the values from the new reversed middle
    and the beginning until the middle pointer reaches the end. 
    """
      def reverse(head):
          prev,curr = None,head
          while curr:
              nxt = curr.next
              curr.next = prev
              prev = curr
              curr = nxt
          return prev

      fast,slow,ans = head,head, 0 

      while fast and fast.next: #find the middle element
          slow = slow.next
          fast = fast.next.next

      mid = reverse(slow) #reverse the list from the middle to the end
      start = head

      while mid:
          ans = max(ans, start.val+mid.val) #this adds the twin sums
          mid = mid.next #while getting the max
          start=start.next

      return rs
