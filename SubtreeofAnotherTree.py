# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
      """
      This is a bit of an extension of another leetcode problem isSubtree (whose solution is in this repo). This problem is easier now that I wrote the 
      code. Basically we define a helper function sametree to tell if two trees are the same. That function is recursive takes a base case of two null
      nodes returning true, if one node is null but the other exists we return true (because one has a node but the other doesn't) and if the 
      two nodes exist and have the same value we call the same function on their left and right nodes. Following this we define our function isSubtree.
      If the subRoot is null we return True because a leaf of the root will point to None so that case will always result in True. If root doesn't exist
      we return because you can't have a subclass of something that doesn't exist. Finally, we compare the node and if they're equal return true.
      Otherwise, we compare subRoot to the nodes and see how those are looking and if we get a match we return True!
      """
        def sametree(p,q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return sametree(p.left,q.left) and sametree(p.right,q.right)
            if not p or not q or p.val != q.val:
                return False
            
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if sametree(root,subRoot):
            return True
        
        if self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot):
            return True
        
        
        
        
