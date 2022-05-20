# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      """
      You iterate through the binary tree and store all the values in a list. Following that you sort the list and select the k-1th element since k is 1 
      indexed. (You iterate through the binary tree recursively by seeing if there is a node and if there is append the value then call the function
      on the left and right children.)
      """
        ans = []
        
        def recurse(node):
            if node:
                ans.append(node.val)
                recurse(node.left)
                recurse(node.right)
        
        recurse(root)
        ans = sorted(ans)
        
        return ans[k-1]
