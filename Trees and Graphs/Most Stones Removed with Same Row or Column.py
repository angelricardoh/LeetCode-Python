# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

# Example 1:

# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Explanation: One way to remove 5 stones is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,1].
# 2. Remove stone [2,1] because it shares the same column as [0,1].
# 3. Remove stone [1,2] because it shares the same row as [1,0].
# 4. Remove stone [1,0] because it shares the same column as [0,0].
# 5. Remove stone [0,1] because it shares the same row as [0,0].
# Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
# Example 2:

# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Explanation: One way to make 3 moves is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,0].
# 2. Remove stone [2,0] because it shares the same column as [0,0].
# 3. Remove stone [0,2] because it shares the same row as [0,0].
# Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
# Example 3:

# Input: stones = [[0,0]]
# Output: 0
# Explanation: [0,0] is the only stone on the plane, so you cannot remove it.

# Constraints:

# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 104
# No two stones are at the same coordinate point.

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def __getitem__(self, item):
         return self.graph[item]
        
    def DFSUtil(self, v, visited):
        visited.add(v)

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
                
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)
        return visited
        
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        visited_list = [None] * n
        graph = Graph()
        for item in stones:
            for edge in stones:
                if item == edge:
                    continue
                if item[0] == edge[0] or item[1] == edge[1]:
                    graph.addEdge((item[0], item[1]), (edge[0], edge[1]))
    
        result = 0
        for item in stones:
            current_node = (item[0], item[1])
            visited = graph.DFS(current_node)
            if visited not in visited_list:
                components_visited = len(visited) - 1
                result += components_visited
                visited_list.append(visited)
            
        return result