# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = []
        right = []
        product = 1
        for i in range(n):
            product *= nums[i]
            left.append(product)
        product = 1
        for j in range(n - 1, -1, -1):
            product *= nums[j]
            right.insert(0, product)
        
        for i in range(n):
            if nums[i] == 0:
                if i - 1 >= 0 and i + 1 < n:
                    result[i] = left[i - 1] * right[i + 1]
                elif i < n:
                    result[i] = left[i - 1]
                else:
                    result[i] = right[i + 1]
            else:
                result[i] = int(left[n - 1] / nums[i])
        return result