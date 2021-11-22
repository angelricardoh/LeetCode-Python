# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 
# Constraints:

# 0 <= rowIndex <= 331

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        dp = [1, 1]

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return dp
        for i in range(2, rowIndex + 1):
            current_dp = []
            current_dp.append(1)
            for j in range(1, i):
                current_dp.append(dp[j - 1] + dp[j])
            current_dp.append(1)
            dp = current_dp
        return dp