class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      """
      For this problem imagine all the numbers lined up on a numberline. The longest consecutive subsequence is really easy to find since it is just the 
      biggest block of connected numbers. From here, it's just a matter of being precise in what we're looking at. It's easy to see where a block starts
      because the starting number of a connected sequence on a numberline will be the number with no number to its left. We can then tell how long the 
      connection is by seeing if the next number is in our list. That's the entire problem. Now for the implementation aspects. The easiest way to check
      what numbers we have in our list is to make a set of the numbers then we iterate through our list to see if the current number we're looking at is 
      the start of a sequence (via the no number to left method) and if it is we check to see how many numbers to the right of it there are.
      """
        numset = set(nums)
        ans = 0
        
        for i in nums:
            if i - 1 not in numset:
                length = 1
                while i+length in numset: 
                    length+=1
                ans = max(ans,length)
                
        return ans
