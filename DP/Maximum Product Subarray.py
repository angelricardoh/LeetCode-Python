# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# It is guaranteed that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution:    
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp_min = [0] * n
        
        dp[0] = nums[0]
        dp_min[0] = nums[0]
        
        for i in range(1, n):
            if nums[i] == 0:
                dp[i] = 0
                dp_min[i] = 0
            else:
                dp[i] = max(dp[i - 1] * nums[i], dp_min[i - 1] * nums[i], nums[i])
                dp_min[i] = min(dp[i - 1] * nums[i], nums[i], dp_min[i - 1] * nums[i])
        return max(dp)