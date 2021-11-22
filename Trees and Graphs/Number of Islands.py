# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 
# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def __getitem__(self, item):
        return self.graph[item]
    
    def DFSUtil(self, node, visited):
        visited.add(node)
        
        neighbours = self.graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
        return visited
        
        
    def DFS(self, node):
        visited = set()
        
        return self.DFSUtil(node, visited)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        graph = Graph()
        m = len(grid)
        n = len(grid[0])
        for j in range(m):
            for i in range(n):
                if i - 1 >= 0 and grid[j][i - 1] == "1":
                    graph.addEdge((j, i), (j, i -1))
                if i + 1 < n and grid[j][i + 1] == "1":
                    graph.addEdge((j, i), (j, i + 1))
                if j - 1 >= 0 and grid[j - 1][i] == "1":
                    graph.addEdge((j, i), (j - 1, i))
                if j + 1 < m and grid[j + 1][i] == "1":
                    graph.addEdge((j, i), (j + 1, i))
          
        visited_list = []
        for j in range(m):
            for i in range(n):
                if grid[j][i] == "1":
                    visited = graph.DFS((j, i))
                    if visited not in visited_list:
                        visited_list.append(visited)
                    
        return len(visited_list)