# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      """
      This is a BFS question. Start with a queue and add the node. From there run bfs and store all the nodes of one level into a list named level and then
      add their children to the end of the queue from left to right order. If level is nonempty we add it to the answer
      """
        ans = []
        q = collections.deque()
        q.append(root)
        
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                ans.append(level)
            
        return ans
