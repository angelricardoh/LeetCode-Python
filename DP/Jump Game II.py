# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[n - 1] = 0
        for i in range(n - 2, -1, -1):
            current_value = 0
            min_value = float('inf')
            for steps in range(1, nums[i] + 1):
                if i + steps > n - 1:
                    break
                current_value = 1 + dp[i + steps]
                if current_value < min_value:
                    min_value = current_value
            dp[i] = min_value
        return dp[0]