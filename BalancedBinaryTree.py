# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      """
      This is efficient to implement as a ground up approach. Based on the problem statement we know that a tree is balanced if the heights of the root nodes
      doesn't differ by more than 1 and we want to keep track of if any of the subnodes from the root is unbalanced. Therefore, we create a function that 
      returns whether the current node is balanced and return the height in the form of a list (we make the function recursive). To conclude, we call the 
      function on the root and return whether the root is balanced (because if any of the subroots is unbalanced then it will have False for it's balanced
      portion of the list). 
      """
        
        def dfs(root):
            if not root:
                return [True,0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = abs(left[1]-right[1]) <= 1 and left[0] and right[0]
            
            return [balanced, 1 + max(right[1],left[1])]
        
        ans =  dfs(root)
        
        return ans[0]
        
        
        
