class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      """
      This is kind of easy. We know that in the matrix the first element of each subsequent list is bigger than the last element of the previous list and
      that all the lists are sorted. So we just need to find the sublist that the target element would belong to if it exists. After we find the list that
      the number would belong to we just run binary search on the sublist that the element would appear in. If we find it we return True and if we don't we
      return False. There are cases where the list the target would belong wouldn't exist so we have check, a flag variable making sure that such a list 
      exists. If the list doesn't exist we return false and if it does we return binary search.
      """
        l,r = 0,-1
        check = False
        
        for sublist in matrix:
            if target >= sublist[l] and target <= sublist[r]:
                search = sublist
                check = True
        
        if check:
            l, r = 0, len(search)

            while l <= r:
                mid = (l+r)//2
                if target > search[mid]:
                    l = mid+1
                elif target < search[mid]:
                    r = mid - 1
                else:
                    return True
        
        return False
