class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """ I forgot to mention you need to set top and bottom pointers since it's a matrix but those are just your left and right pointers. 
        This is something you'll need to visualize. Pretty much for each iteration you're rotating the outermost matrix and once those iterations are 
        complete you're treating the smaller matrices as a subproblem. For example, in a 4x4 matrix in the first iteration you're rotating everything
        in the corners but you're doing it in reverse order. So you save the element found in the top left of the matrix you're rotating and store it 
        in a variable. Then you fill it with the element underneath it. Then you fill the element in the bottom left with the element in the bottom right
        and fill the element in the bottom right with the element above it. Finally you fill the element in the top right with the element you stored away
        in the beginning which is the original top left element. Now you have the method of rotating down and clear you have to figure out how you 
        will rotate the entire matrix and what you will do is you will move your starting point to the right by the amount i for the amount of columns
        you have to rotate which will be columns -1 (since the number in the last position of that column gets filled in with the first). From there you
        do similar things for all of the other things as well. Finally to increment our pointers we want to add 1 to l and subtract 1 from r and go until
        our pointers cross.
        """
        l,r = 0,len(matrix)-1
        
        while l<r:
            for i in range(r-l):
                top,bottom = l,r
                #save the top left variable
                topleft = matrix[top][l+i]
                #move the bottom left to the top left
                matrix[top][l+i] = matrix[bottom-i][l]
                #move the bottom right to the bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                #move the bottom right to the bottom left
                matrix[bottom][r-i] = matrix[top+i][r]
                #move the bottom left to the top right
                matrix[top+i][r] = topleft
                
            l,r = l+1,r-1
                
