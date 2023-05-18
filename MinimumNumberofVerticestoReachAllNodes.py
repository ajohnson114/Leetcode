def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
  """
  Basically, the trick to notice in this problem that the minimum set of vertices that you would need to know to
  traverse the graph would be the nodes with no inbound connections since given the problem says that this is a DAG
  there is no cycle or indegree to reach a node with no inbound connection and those with an inbound connection can be
  reached by those without one in all the examples. Thus we just need to make an array that holds inbound counts and loop
  through the edges and increment the node everytime we see it has an inbound connection. At the end we return the node
  if it has an indegree of 0 (i.e. no inbound connections).
  """
        deg = [0] * n 

        for u, v in edges:            
            deg[v] += 1

        return [node for node in range(n) if deg[node] == 0]
