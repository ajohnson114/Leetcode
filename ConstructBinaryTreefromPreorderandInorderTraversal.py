# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
      """
      This is best done with a picture but we're constrained by text here. Inorder traversal simply means scanning the binary tree left to right so looking
      at the left most node all the way to the right most node. Preorder traversal looks at the root, then the left node and then recurses on the left node 
      and then the right node it recurses on that.
      
      Two things are guaranteed here. 1 That in the beginning the first element in the preorder list will be the root and 2 that everything before the root
      value in the inorder list will be on the left side of the tree. Finally since they've guaranteed that all values are unique we've practically solved 
      the question. First we check to see that both lists have values in them and if they don't return None since that is our base case. Next as previously
      mentioned our root node is the first element of preorder. Then we find what value splits the tree in two and then take its index which works since
      all values are unique here. Then we recursively call the function for the left subtree and right subtree. For the left subtree, we want the preorder
      list but just the values from 1 until the midpoint which makes sense because the preorder traversal looks at the entire left tree before moving to the
      rightt. So in python we do [1:mid+1] since the ending index doesn't get included and for the inorder list we want everything but the the midpoint array
      since the midpoint is the root. Next for the right subtree we want everything that didn't get included in the last function call so preorder[mid+1:] 
      and for the inorder list we want to get everything but the root index. Finally we can return the root since that is the head of the answer.
      """
        if not preorder and not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        
        return root
        
