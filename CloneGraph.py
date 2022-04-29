"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Use a hashmap and recursive dfs and map the old nodes to the copy nodes. Map the first node to the new node and then go to its first neighbor and start cloning there. For each of the subsequent nodes we'll look to see the neighbors and if those nodes are in the hash map look those up and then connect the copies to the new copy. The base case is when you reach a full cycle and in that case you will cycle all the way back up top and check all your other nodes to see if all connections are made in your starting node.
        """
        
        oldtonew = {}
        
        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]
            new = Node(node.val)
            oldtonew[node] = new
            
            for i in node.neighbors:
                new.neighbors.append(dfs(i))
            
            return new
        
        return dfs(node) if node else None
