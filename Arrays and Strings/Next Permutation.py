# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]

# Example 4:

# Input: nums = [1]
# Output: [1]

# Constraints:

#     1 <= nums.length <= 100
#     0 <= nums[i] <= 100

import copy
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
#         for i in range(n - 2, -2, -1):
#             min_diff = float('inf')
#             index_min_diff = -1
#             for j in range(i + 2, n):
#                 if nums[j] - nums[i + 1] > 0 and nums[j] - nums[i + 1] < min_diff:
#                     min_diff = nums[j] - nums[i + 1]
#                     index_min_diff = j
            
#             if index_min_diff == -1:
#                 continue
#             aux = nums[index_min_diff]
#             nums[index_min_diff] = nums[i + 1]
#             nums[i + 1] = aux
#             aux_array = nums[i + 2:]
#             aux_array.sort()
#             nums[i + 2:] = aux_array
#             return nums
#         return nums.sort()
    
        for i in range(n - 1, -1, -1):
            min_diff = float('inf')
            index_min_diff = -1
            for j in range(i + 1, n):
                if nums[j] - nums[i] > 0 and nums[j] - nums[i] < min_diff:
                    min_diff = nums[j] - nums[i]
                    index_min_diff = j
            
            if index_min_diff == -1:
                continue
            aux = nums[index_min_diff]
            nums[index_min_diff] = nums[i]
            nums[i] = aux
            aux_array = nums[i + 1:]
            aux_array.sort()
            nums[i + 1:] = aux_array
            return nums
        return nums.sort()
            
            
