# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
 
# Constraints:

# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = float('inf')
        min_sum = None
        n = len(nums)
        
        nums.sort()
        
        for i in range(n - 2):
            left_pointer = i + 1
            right_pointer = n - 1
            
            while left_pointer != right_pointer:
                current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
                # print(str(nums[i]) + ' ' + str(nums[left_pointer]) + ' ' + str(nums[right_pointer]))
                diff_target = abs(target - current_sum)
                # print(diff_target)
                if diff_target < min_diff:
                    min_diff = diff_target
                    min_sum = current_sum
                    
                if current_sum < target:
                    left_pointer += 1
                else:
                    right_pointer -= 1
                    
        return min_sum