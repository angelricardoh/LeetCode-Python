# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         zigzag = False
#         result = []
#         def bfs(node):
#             if not node:
#                 return
            
#             nonlocal zigzag
#             nonlocal result
#             queue = [(node, 0)]
#             visited = set()
#             result.append([node.val])
#             level = 0
            
#             while queue:
#                 current_node, current_level = queue.pop(0)
#                 if current_node not in visited:
#                     visited.add(current_node)
                    
#                     if len(result) <= current_level + 1:
#                         result.append([])
#                     if current_node.left:
#                         queue.append((current_node.left, current_level + 1))
#                     if current_node.right:
#                         queue.append((current_node.right, current_level + 1))
#                     if current_node.right and current_node.left:
#                         if zigzag:
#                             result[current_level + 1].append(current_node.left.val)
#                             result[current_level + 1].append(current_node.right.val)
#                         else:
#                             result[current_level + 1].append(current_node.right.val)
#                             result[current_level + 1].append(current_node.left.val)
#                         zigzag = not zigzag
#                     elif current_node.right:
#                         result[current_level + 1].append(current_node.right.val)
#                     elif current_node.left:
#                         result[current_level + 1].append(current_node.left.val)
        
#         bfs(root)
#         if len(result) != 0:
#             result.pop()
#         return result
    
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        results = []
        def dfs(node, level):
            if level >= len(results):
                results.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node is not None:
                    dfs(next_node, level+1)

        # normal level order traversal with DFS
        dfs(root, 0)

        return results