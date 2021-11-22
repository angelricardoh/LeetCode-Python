# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]
from collections import defaultdict 

class Solution:
    
    WHITE = 1
    GRAY = 2
    BLACK = 3
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        topological_sort = []
        colors = {k: Solution.WHITE for k in range(numCourses)}
        is_cycle = False
        
        class Graph:
            def __init__(self):
                self.graph = defaultdict(list)

            def addEdge(self, u, v):
                self.graph[u].append(v)

            def dfs(self, u):
                nonlocal is_cycle
                if is_cycle:
                    return
                
                colors[u] = Solution.GRAY
                
                for neighbour in self.graph[u]:
                    if colors[neighbour] == Solution.WHITE:
                        self.dfs(neighbour)
                    elif colors[neighbour] == Solution.GRAY:
                        is_cycle = True
                
                colors[u] = Solution.BLACK
                topological_sort.append(u)
            
        graph = Graph()
        for item in prerequisites:
            graph.addEdge(item[1], item[0])
        
        for vertex in range(numCourses):
            if colors[vertex] == Solution.WHITE:
                graph.dfs(vertex)
        
        if is_cycle:
            return []
        return topological_sort[::-1]