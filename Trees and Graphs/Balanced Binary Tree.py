# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        leveled = True
        def backtrack(root, level = 0):
            nonlocal leveled
            if not root:
                return level
            
            level_left = level
            level_right = level
            level_left = backtrack(root.left, level + 1)
            level_right = backtrack(root.right, level + 1)
            
            if abs(level_left - level_right) >= 2:
                leveled = False
                
            return max(level_right, level_left)
                    
        backtrack(root)
        return leveled
        