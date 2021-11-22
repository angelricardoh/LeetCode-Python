# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
# Example 4:

# Input: nums = [1,3,5,6], target = 0
# Output: 0
# Example 5:

# Input: nums = [1], target = 0
# Output: 0

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = self.searchRec(nums, target, 0, len(nums) - 1)
        return index
        
    def searchRec(self, nums: List[int], target: int, low: int, high: int) -> int:   
        middle = int((high + low) / 2)
        
        if high < low and nums[middle] < target:
            return middle + 1
        if high < low and nums[middle] > target:
            return middle
    
        if target == nums[middle]:
            return middle
        elif target < nums[middle]:
            return self.searchRec(nums, target, low, middle - 1)
        else:
            return self.searchRec(nums, target, middle + 1, high)
            