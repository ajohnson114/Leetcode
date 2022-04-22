# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      """
      The lowest common ancestor is the node at which the first bifurcation in the search space of the tree occurs. So if one is less than and one is greater
      then that is the lowest common ancestor. So we must check the cases where they are both less than or greater than and search left and right respectively
      . Otherwise return the current value. We start always start at the root and check from there.
      """
        curr = root
        
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
