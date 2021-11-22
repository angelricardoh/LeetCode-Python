# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        min_index = float('inf')
        max_index = float('-inf')
        
        def binary_search(nums, left, right, target):
            nonlocal min_index
            nonlocal max_index
            if left > right:
                return
            
            mid = int((left + right) / 2)
            
            if nums[mid] == target:
                if mid < min_index:
                    min_index = mid
                if mid > max_index:
                    max_index = mid
                binary_search(nums, left, mid - 1, target)
                binary_search(nums, mid + 1, right, target)
                return
            
            if nums[mid] > target:
                binary_search(nums, left, mid - 1, target)
            else:
                binary_search(nums, mid + 1, right, target)
        
        n = len(nums)
        binary_search(nums, 0, n - 1, target)
        if min_index == float('inf') and max_index == float('-inf'):
            return [-1, -1]
        return [min_index, max_index]        