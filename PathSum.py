"""
Retrospectively this one isn't too bad. What we do is recursive subtract the current node value from the target and call the function on the children. If 
either one of them has a value that is equal to our new subtracted sum and doesn't have children (since it has to be a leaf) then we can return True.
If we keep going until there is nothing there then we can return False. That's pretty much it
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        targetSum -= root.val
        
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
