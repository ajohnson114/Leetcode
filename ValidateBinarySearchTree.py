# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      """
      To start this problem we know that the root can be any number so we want to have upper and lower bounds to compare it to so +- infinity can be those
      bounds. If the node is bigger than the left bound and smaller than the right it is valid. So we check that we have a node and then check that condition
      and if it passes then we call it on both of its children. To check it's left child we set the right bound to be the parent node value since we know 
      that in a binary search tree the left child must be smaller than the parent similarly we call the function on the right child and set the left bound 
      equal to the parent node value since we know that in a bst the right child should be greater than the parent. Finally we can simply return the dfs 
      call on the root with the left and right bounds of negative infinity.
      """
        def dfs(node, left,right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
          
        return dfs(root, float("-inf"),float("inf"))
