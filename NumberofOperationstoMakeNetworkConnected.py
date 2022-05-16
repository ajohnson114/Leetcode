class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
      """
      This is a use of Union find. The algorithm in its most efficient form uses a rank comparison and is broken into 2 parts - Union and find. The find 
      portion takes in a node and outputs the parent of the node (In the beginning of our code we should instantiate 2 lists. One consisting of ranks 
      where each node has a rank of 1 and a second consisting of all the nodes since each node is it's own parent.). It does this by (in its most efficient
      form) finding the parent of the node and then if the parent of the node is not equal to its own parent we can set the parent of the node equal to 
      it's own great grandfather (we can also set it equal to its own parent but that would be a bit slower). Then once the parent of the node is equal to 
      its own parent then we can return the parent. The union portion takes in two nodes and calls the find algorithm. If the two nodes have the same parent
      then we know that they can't be joined without creating a redundant connection so we can return False in that case. If they don't share the same parent
      then we can compare the ranks of the two nodes and when one is greater than the other we can set the parent of the smaller ranked node to be equal to
      the parent of the bigger ranked one and add the current rank of the smaller ranked one to the bigger ranked one and then return true.
      
      This utilizes Union-Find which I've explained in another file and I'll leave the explanation above. But if the length of connections is smaller
      than n-1 then we know that there isn't enough cables to connect the computers. Furthermore, when we find a union we want to subtract 1 from the amount
      of connections we need since we know we'll need n-1 connections to connect the computers. So we can just return n-1 for our answer. 
      """
        parent = [i for i in range(n)]
        rank = [1]*n
        
        def find(node):
            p = parent[node]
            while p!=parent[p]:
                p = parent[parent[parent[p]]] #compress the path
            return p
        
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        count = 0
        
        if len(connections) < n-1:
            return -1
        
        for n1,n2 in connections:
            if union(n1,n2):
                n-=1
        
        return n-1
