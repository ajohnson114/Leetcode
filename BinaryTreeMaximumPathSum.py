def maxPathSum(self, root: Optional[TreeNode]) -> int:
  """
  To split or not to split that is the question. Basically to split or not split means to take both the children or to
  take the path from the parent and 1 child and then go back up. So to do this we can initiliaze an answer variable with 
  the root value in it. Then create a dfs function. The base case will be a null node and in that case we return 0 since 
  the math path we can take is 0. After this we do 2 recursive calls on the children and then check to see if they are 
  negative or not in which case we will say they are 0. Then we check to see if the path we can make with splitting 
  ie taking the node and its children is bigger than the answer variable and then we return the max path w/o splitting
  i.e. the max path of the node and the bigger of the 2 children paths. We call the function on the root and then return
  our answer variable
  """
        res = [root.val]

        #return max pathsum w/o splitting
        def dfs(node):
            if not node:
                return 0

            leftmax = dfs(node.left) 
            rightmax = dfs(node.right) 
            leftmax = max(leftmax, 0)
            rightmax = max(rightmax,0)
            
            #compute maxpath sum with split
            res[0] = max(node.val + leftmax + rightmax, res[0])

            maxpath = node.val + max(leftmax, rightmax)
            return maxpath

        dfs(root)
        return res[0]
