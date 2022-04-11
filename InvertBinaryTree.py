# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Recursive solution. Base case: You reach the end of the tree and you were passed to the leaf which has no children hence you evaluate on self.left 
    and self.right which are both None types so you return None. Outside of that we want to return a node with a value we're currently at but with
    the children switched around so we call the same function recursively with the appropriate variables.
    """
        if not root:
            return None
        newtree = TreeNode(root.val)
        newtree.right = self.invertTree(root.left)
        newtree.left = self.invertTree(root.right)
        return newtree
