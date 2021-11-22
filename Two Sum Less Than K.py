# Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

# Example 1:

# Input: nums = [34,23,1,24,75,33,54,8], k = 60
# Output: 58
# Explanation: We can use 34 and 24 to sum 58 which is less than 60.
# Example 2:

# Input: nums = [10,20,30], k = 15
# Output: -1
# Explanation: In this case it is not possible to get a pair sum less that 15.

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = -1
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < k and nums[i] + nums[j] > result:
                    result = nums[i] + nums[j]
        
        return result