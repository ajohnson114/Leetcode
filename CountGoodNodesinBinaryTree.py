# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
      """
      DFS question. Basically do a dfs on the root and if the node value you're looking at is bigger than the biggest value you've seen so far it's a good
      node otherwise it isn't. The base case is a null root so return 0 otherwise result is 1 if it's a good node and 0 else. Make sure you update your max
      value to what ever is biggest and then call the same function on the children and add the result of that call to your current result. Finally return 
      result. The answer is the function call on the root and the root value.
      """
        def dfs(node, maxval):
            if not node:
                return 0
            res = 1 if node.val >= maxval else 0
            maxval = max(maxval, node.val)
            res += dfs(node.left, maxval)
            res += dfs(node.right, maxval)
            return res
        
        return dfs(root, root.val)
