# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      """
      The depth of each node is 1 + the biggest depth of each of its children. This code has an invisible base case where once a node doesn't have a child 
      it runs maxDepth on itself and sees that root is False so it returns 0 and the root that didn't have any child gets the value of 1 and then traverses
      back upwards. Pretty easy conceptually.
      """
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return 0 
