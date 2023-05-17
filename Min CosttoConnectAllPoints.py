def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Prim's Algorithm: O(e^2 log(e)) time-> main idea BFS + priority queue (instead of queue in BFS) ; also you will be 
        adding duplicates hence complexity to pop from the min-heap is n^2*log(n)

        visit: hashset frontier: minheap
        We need to find n-1 edges to connect n points with no cycle. In this scenario we also want to minimize the cost of 
        those edges. Basically in the first implementation we precomute the distance from point i to j and add each distance
        and point index to the adjacency list of the other node since we are working with a doubly connected graph. Following
        that we set our set and minHeap and prims algorithm is ready to go. We know that we're done when the visited set is 
        full but at each iteration we want to pop from the heap (take the closest element), check to see if we've visited it
        if we have continue. Otherwise, we add the cost to the result, add the point to the visited set and then go through
        the adjacency list of the point and if those aren't in visited we add them to the heap. Once we've visited all the 
        nodes we can return the answer. 
        
        The second implementation doesn't precompute the distances for the point and does it ad hoc for each other point
        it cuts the implementation approximately in half
        """
        
        l1_norm = lambda x1,x2,y1,y2 : abs(x1-x2) + abs(y1-y2)
        N = len(points)
        adj = {i:[] for i in range(N)}

        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                dist = l1_norm(x1,x2,y1,y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        #Prim's Algorithm    
        res = 0
        visit = set()
        minheap = [[0,0]] #cost, point

        while len(visit) < N:
            cost,i = heapq.heappop(minheap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minheap,[neiCost,nei])

        return res

        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        pq = [(0, tuple(points[0]))]
        mincost = 0
        toVisit = set([tuple(x) for x in points])

        while pq:
            curCost, curNode = heapq.heappop(pq)
            if curNode not in toVisit:
                continue
            toVisit.remove(curNode)
            mincost += curCost
            if len(toVisit) == 0:
                break
            for n in toVisit:
                heapq.heappush(pq, (manhattan(curNode, n), n))
        
        return mincost
