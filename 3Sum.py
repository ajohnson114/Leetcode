def threeSum(self, nums: List[int]) -> List[List[int]]:
"""The key to tackling this sum is to realize that you can iterate through this sorted list and then just do 2sumIIsorted on the rest of the elements.
The else case is the only tricky part. You have to imagine a situation like this [-2,-2,0,0,2,2] where you need to iterate your pointer multiple times
you can do this by making sure you're not on the same value as you were last time to avoid duplicates and you also need to make sure you're within 
the original constraints. Your conditions will update the other pointer so no need to worry about that. 
All in all assuming you've done 2SumIISorted it's not that bad except for that one test case.
"""

        nums = sorted(nums)
        l,r = 0 ,len(nums)-1
        ans = []
        
        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
                
            l,r = i+1,len(nums)-1
            
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -=1
                elif threesum < 0:
                    l += 1
                else:
                    ans.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l <r:
                        l +=1
        return ans
