class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
      """
      This is an extension of Course schedule 1 and uses a similar algorithm. Long story short, you use dfs on each of the nodes and each of their children
      if there is a cycle you return False and if you've visited it before you know that that course is fine in regards to being able to take prereqs 
      therefore you return True. So when you see a node add it to the cycle set then run dfs on it's children and if all that works out then remove it from
      the cycle and add it to visited. Once you do all that you can add it to ans which is your output variable. Finally, run dfs on all your nodes and if 
      any of the function calls return False then you should return False. If none of them return False which in this case is an empty list otherwise
      you can return the answer variable
      """
        prereq = {i:[] for i in range(numCourses)}
        
        for crs, req in prerequisites:
            prereq[crs].append(req)
        
        #There are 3 possible states
        #visited -> course added to output
        #visiting -> course not added to output but added to cycle
        #unvisited -> course not added to output or cycle
        
        ans = []
        
        visited = set()
        cycle = set()
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for i in prereq[course]:
                if not dfs(i):
                    return False
            cycle.remove(course)
            visited.add(course)
            ans.append(course)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return ans
            
