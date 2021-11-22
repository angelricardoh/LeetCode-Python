# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        dp_forward = [0] * n
        dp_backward = [0] * n
        max_pass = float('-inf')
        
        for i in range(n):
            if height[i] > max_pass:
                max_pass = height[i]
                
            dp_forward[i] = max_pass - height[i]
            
        max_pass = float('-inf')
        for i in range(n - 1, -1, -1):
            if height[i] > max_pass:
                max_pass = height[i]
                
            dp_backward[i] = max_pass - height[i]
            
        dp = [0] * n
        for i in range(n):
            dp[i] = min(dp_forward[i], dp_backward[i])
            
        result = 0
        for item in dp:
            result += item
        
        return result