def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
  """
  Essentially this is the merging part of merge sort. What we're gonna do is traverse the list and merge each linkedlist
  that is next to each other while the length of the lists variable is greater than 1. So we can do this by traversing the 
  lists variable merging 2 linkedlists at a time and then adding it to a temporary variable we'll call mergedlist then 
  reassigning the lists variable to mergedlist. When this is done we need to return the first element of lists. To merge
  2 linkedlists we just need to implement an earlier leetcode problem. Basically while there are still 2 nonempty linkedlists
  we should do the 2 finger algorithm and if one is lower than the other we add that to the dummy list then update the list
  we just took a value from and the list we just added to. When both lists no longer exist we just need to append the list
  that is still there to the answer and return the answer.
  """
        if not lists or len(lists) ==0 :
            return None
        while len(lists) > 1:
            mergedlist = []
            
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedlist.append(self.merge(l1,l2))
            
            lists = mergedlist
        return lists[0]

    def merge(self,a,b):
        dummy = ListNode()
        tail = dummy

        while a and b:
            val1 = a.val if a else 0
            val2 = b.val if b else 0
            if val1 > val2:
                tail.next = ListNode(val2)
                b = b.next
            else:
                tail.next = ListNode(val1)
                a = a.next
            tail = tail.next

        if a:
            tail.next = a
        if b:
            tail.next = b

        return dummy.next
