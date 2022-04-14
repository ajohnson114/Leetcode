# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      """
      This problem has 2 components. To tell what the largest diameter is you need to figure out the heights of all the nodes as the diameter for the node
      will be the sum of both subnodes. To find the heights we employ recursion and say that the height of our current node is 1 + the biggest height of 
      its children. Therefore, we instantiate a global constant to store the biggest diameter found so far, use recursion to find the heights of all the 
      children, compute the diameter for each node and if it's bigger than the biggest diameter we've found so far. Finally we call our function on our root
      and then return the global variable that was adjusted by our recursive function. 
      """
        biggest = [0]
        
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            biggest[0] = max(left + right, biggest[0])
            
            return 1 + max(left,right)
        
        dfs(root)
        
        return biggest[0]
