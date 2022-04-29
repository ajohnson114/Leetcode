class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      """
      You want to instantiate 4 pointers that will signify the top, bottom, left and right bounds for your matrix but you would like for right and bottom
      to be techincally out of bounds for your matrix because that will make looping through the array simpler. From here we will make a spiral but once
      we dont need to look at a row or column anymore we will increment/decrement that pointer and proceed with our algorithm. From here it's sort of 
      simple. You need to make sure you pointers are valid so set that as the condition for your while loop. Then go through the top row iterating from
      left to right and get all the elements. You no longer need the top row so you can increment that pointer then move onto getting everything in the 
      right column once you do that you can increment the right pointer. Now you need to check if your pointers are still valid so we should check our while
      loop conditions since there can be a case of a column vector or something of the sort that may give us an error. Then we iterate through the bottom
      row which we have to do by going backwards so (r-1,l-1,-1) and then we decrement our bottom pointer and then we do the same for the numbers in the
      left column so we can do from bottom to top and add all the numbers. Finally after all that we can increment the left pointer and then continue 
      our loop. After all that we can return our answer.
      """
        l,r = 0, len(matrix[0]) #adjusts columns
        top = 0 #adjust rows
        bottom = len(matrix) #adjust rows
        res = []
        while l<r and top < bottom:
            #get every i in the top row
            for i in range(l,r):
                res.append(matrix[top][i])
                
            top+=1 #we no longer need this row 
            
            for i in range(top,bottom):
                res.append(matrix[i][r-1])
            
            r-=1 #we no longer need this portion of the matrix
            
            if not (l<r and top < bottom): #imagine a column vector etc
                break
            
            #get every i in the bottom row
            for i in range(r-1,l-1,-1):
                res.append(matrix[bottom-1][i])
            
            bottom -=1
            
            #get every i in the left column
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][l])
            
            l+=1
        
        return res
                
