def LIS(arr):

""""The way to approach this answer is with Dynamic Programming. We want to see what the Longest Increasing Subsequence(LIS) starting at position i is
one can think that we can come up with a recursive solution where each element asks for all the elements that are bigger than me what is the longest
increasing subarray starting at their index I'll get that answer and add one to them. From here we build our answer. The base case is 1 as the longest
increasing subsequence of a single element is itself. So we go backwards through the list and from the pointer that we go backwards from we then check 
all the elements in front to see what the longest increasing subarray starting from their indices and if it's bigger than the LIS at our current index
we set ours to 1 + the LIS at theirs"""

    LIS = [1]*len(arr)
    for i in range(len(arr)-1,-1,-1): #this iterates through the list backward
        for j in range(i+1,len(arr)): #this goes from the previous pointer to the end of the list
            if arr[i] < arr[j]: #check to see if the number in front of the number you're currently at is bigger
            LIS[i] = max(LIS[i], LIS[j]+1) #if the longest increasing subarray starting at pos j > LIS starting at pos i 
            #make the LIS starting at index i the bigger of the one starting at j + 1 since we're adding i to that subarray and it's own LIS
  return max(LIS) #return the largest increasing subarray
