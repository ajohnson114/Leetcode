def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
  """
  a = [1,2,3,4,5] b = [1,2,3,4,5,6,7,8,9,10] joined = [1,1,2,2,3,3,4,4,5,5,6,7,8,9,10] median = 4
  left partition = [1,1,2,2,3,3,4] len = 7 right partition = [5,5,6,7,8,9,10] len = 7
  total = 15 half = 7 
  i = 2 j = 2
  aleftpartition = [1,2,3] bleftpartition = [1,2,3]
  aleft = 3 bleft = 3 total is odd so return min(a[i+1],b[j+1]) == 4
  
  To answer this questions we should strictly define what a median is. In this scenario, we will say that a median is a 
  number that perfectly partitions an array in 2. Based on this idea, we know that if we added the two arrays together in
  sorted order we would be able to find the median very easily but due to the time constraints on this problem that is out
  of the question so we must get around that. Essentially what we want to do is figure out 2 positions in each array to 
  form the left partition of the joined array and then use the 2 formed partitions to find the median. In the even case,
  the median will be the [-1] element of the left partition + the [0] element of the right partition divided by 2. In this
  case we need to take the max of bleft and aleft + the min of aright +bright and divide that in 2. This is because we are
  essentially taking the right most value of the left partition adding it the left most value of the right partition and
  dividing it in 2. The same logic goes for the opposite case barring some minor changes.In the odd case we would just like
  to return the [0] element of the right partition. So since our partition is divided in the 2 arrays we need to find the 
  minimum of the 2 next elements in a and b (labeled aright and b right). 
  
  To even check for the median we must first make sure to make sure that we have the correct partitions. The condition that
  lets us know that we have the right partition is if the right most element in the left partition is smaller than that in
  the left most in the right partition. To check this aleft must be smaller or equal to bright and bleft <= aright. In the 
  case that aleft>bright then we've selected a number that is too high in our a array and we must decrease it so we do so
  by changing it to i-1. The final case is when we've selected a number that is too low in our a array and must increase it
  in which case we change it to i+1. That solves the problem
  """
        a,b = nums1, nums2
        total = len(b) + len(a)
        half = total //2

        if len(b) < len(a): #set up to make sure a is always smaller than b
            a,b = b,a
        

        l,r = 0,len(a)-1
        while 1:
            i = (l+r)//2 #pointer for a
            j = half - i -2 #pointer for b.  -2 is for 0 based indexing (-1 for each array)

            aleft = a[i] if i >= 0 else float('-inf') #this makes sure that i is in range
            aright = a[i+1] if i+1 < len(a) else float('inf') #this makes sure that i+1 is in range
            bleft = b[j] if j >= 0 else float('-inf') #this makes sure that j is in range
            bright = b[j+1] if j+1 < len(b) else float('inf') #this makes sure that j+1 is in range

            #partition is correct
            if aleft <= bright and bleft <= aright:
                if total%2 == 1:
                    return min(aright,bright) #In the odd case we just want the midpoint 
                else:
                    return (max(aleft,bleft) + min(aright,bright))/2 #take [-1] of left partition and [0] of right partition
            elif aleft > bright:
                r = i-1
            else:
                l = i+1
