class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
      """
      This is a use of Union find. The algorithm in its most efficient form uses a rank comparison and is broken into 2 parts - Union and find. The find 
      portion takes in a node and outputs the parent of the node (In the beginning of our code we should instantiate 2 lists. One consisting of ranks 
      where each node has a rank of 1 and a second consisting of all the nodes since each node is it's own parent.). It does this by (in its most efficient
      form) finding the parent of the node and then if the parent of the node is not equal to its own parent we can set the parent of the node equal to 
      it's own great grandfather (we can also set it equal to its own parent but that would be a bit slower). Then once the parent of the node is equal to 
      its own parent then we can return the parent. The union portion takes in two nodes and calls the find algorithm. If the two nodes have the same parent
      then we know that they can't be joined without creating a redundant connection so we can return False in that case. If they don't share the same parent
      then we can compare the ranks of the two nodes and when one is greater than the other we can set the parent of the smaller ranked node to be equal to
      the parent of the bigger ranked one and add the current rank of the smaller ranked one to the bigger ranked one and then return true. We can then call
      union on all the nodes in the edges list and then return the first edges that make union return False
      """
        parent = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)
        
        def find(node):
            p = parent[node]
            
            while p != parent[p]:
                p = parent[parent[p]] #path compression
                p = parent[p]
            
            return p
        
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            
            if p1 == p2:
                return False #this means redundant connection
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1]+=rank[p2]
            else:
                parent[p1] = p2
                rank[p2]+=rank[p1]
                
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
            
            
        
        
