"""
Your objective is to find any peak so you can think of the sequence being a composition of an increasing sequence and that of a decreasing sequence. 
Using this we can construct a binary search such that if the middle element is bigger than the element on it's right we know that it's part of a decreasing
sequence so we should reduce the search space to the elements to its left. Furthermore, we can do the opposite as we can assume that the middle element is
a part of an increasing sequence so we set the search space to the right of mid. After iterating like this we can assume that the final answer is the peak
so we return l.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,len(nums)-1
        
        while l<r:
            mid = (l+r)/2
            if nums[mid]>nums[mid+1]:
                r=mid
            else:
                l = mid+1
        
        return l
