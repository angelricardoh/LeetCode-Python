# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Example 1:

# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# Example 3:

# Input: m = 7, n = 3
# Output: 28
# Example 4:

# Input: m = 3, n = 3
# Output: 6

# Constraints:

# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 109.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(m)] for _ in range(n)]
        if m > 1:
            dp[0][1] = 1
        if n > 1:
            dp[1][0] = 1
        for j in range(0, n):
            for i in range(0, m):
                if (i == 0 and j == 1) or (i == 1 and j == 0) or (i == 0 and j == 0):
                    continue
                up = 0
                left = 0
                if j - 1 >= 0:
                    up = dp[j - 1][i]
                if i - 1 >= 0:
                    left = dp[j][i - 1]
                dp[j][i] = up + left
        result =  min(dp[j][i], 2000000000)
        return result