# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction. 

# Example 1:

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

# Example 2:

# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]

# Example 3:

# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]

# Constraints:

#     1 <= equations.length <= 20
#     equations[i].length == 2
#     1 <= Ai.length, Bi.length <= 5
#     values.length == equations.length
#     0.0 < values[i] <= 20.0
#     1 <= queries.length <= 20
#     queries[i].length == 2
#     1 <= Cj.length, Dj.length <= 5
#     Ai, Bi, Cj, Dj consist of lower case English letters and digits.

import copy
class Solution:   
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        class Node:
            def __init__(self, val):
                self.val = val
                self.edges = []
                self.parent = None
                # self.visited = False
        graph = {}
        n_equations = len(equations)
        n_queries = len(queries)
        results = [-1] * n_queries
        
        for i in range(n_equations):
            equation = equations[i]
            if equation[0] not in graph:
                graph[equation[0]] = Node(equation[0])
            if equation[1] not in graph:
                graph[equation[1]] = Node(equation[1])
            
            # Edge = tuple(value, extreme)
            graph[equation[0]].edges.append((values[i], equation[1]))
            graph[equation[1]].edges.append((1 / values[i], equation[0]))
        
        for index_query, query in enumerate(queries):
            graph_copy = copy.deepcopy(graph)
            queue = [query[0]]
            visited = []
            
            if query[0] not in graph_copy:
                continue
            
            while queue:
                current_value = queue.pop(0)
                if current_value not in graph_copy:
                    continue
                current_node = graph_copy[current_value]
                visited.append(current_value)
                
                if current_node.val == query[1]:
                    break
                
                for edge in current_node.edges:
                    if edge[1] not in visited:
                        queue.append(edge[1])
                        if edge[1] in graph_copy:
                            # print(edge[1])
                            graph_copy[edge[1]].parent = current_node
                        
            if current_node.val != query[1]:
                continue
                
            # backtrack
            backtrack_node = current_node
            result = 1
            while current_node.parent:
                parent_val = current_node.parent.val
                for edge in graph_copy[parent_val].edges:
                    if edge[1] == current_node.val:
                        result *= edge[0]
                        break
                current_node = current_node.parent

            results[index_query] = result
        return results