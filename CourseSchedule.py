class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        We'd like to see if there are any loops in the graph and we'd like to do that by running dfs on each node. Before that we have to do some prep work 
        though. First we instantiate a dictionary where the keys are the courses and the values are empty lists. We do this so that we can store the courses
        prerequirements into the lists. Then we proceed with dfs and maintain a set to see which courses we've visited before. The algorithm proceeds as 
        follows: an empty list means that the course can be completed with no prereqs so we can return True while the course being in our set means that 
        there is a cycle in the graph and we must return False. Following those base cases we can add the course we just visited to the set and then run dfs
        and all of its children and if any of those return False then we should return False as well. Following all of that we remove the node we were just
        in from the visited set and reset the prereqs list of the course to be empty since we know that all of the prereqs can be completed and we return 
        True. Finally, we must call our dfs function on all the courses since we might run into the case of an incomplete graph which would give us 
        incorrect results otherwise and if none of those return False then we can return True.
        """
        premap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)
         
        #stores all the courses along the dfs set
        visited = set()
        
        def dfs(course):
            if course in visited: #this detects a loop
                return False
            
            if premap[course] == []: #if the 
                return True
            
            visited.add(course)
            
            for pre in premap[course]:
                if dfs(pre) == False:
                    return False
            
            visited.remove(course)
            premap[course]=[]
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True
                
            
            
            
        
        
