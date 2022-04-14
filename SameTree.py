# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      """
      Recursive dfs problem. We want the roots of both trees to be the same and then the right and left nodes to be equal too so we define a base case
      where if they're both empty it's true and a second where if the values are different or one of them don't exist we return False. Finally having
      covered all our base cases we return whether the left and right nodes are the same. 
      """
        if not p and not q:
            return True
        
        if (not p or not q) or (p.val != q.val):
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
