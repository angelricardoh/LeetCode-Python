# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 
# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import List

class Solution:
    # Hashing
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        n = len(nums)
        
        for i in range(n):
            hashmap[nums[i]] = i
            
        result = []
            
        for i in range(n):
            for j in range(i + 1, n):
                target = (nums[i] + nums[j]) * -1

                if target in hashmap:
                    complement = hashmap[target]
                    if complement and complement != i and complement != j:
                        element = [nums[i], nums[j], nums[complement]]
                        element.sort()
                        if element not in result:
                            result.append(element)
                        
        return result

    # Two pointers
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        left = 0
        right = 2
        result = []
        
        nums.sort()
        
        for i in range(1, n - 1):
            left = i - 1
            right = i + 1
            if left < 0 or right > n - 1:
                continue
                
            while left >= 0 and right <= n - 1:
                if nums[i] + nums[left] + nums[right] == 0 and [nums[i], nums[left], nums[right]] not in result:
                    result.append([nums[i], nums[left], nums[right]])
                elif  nums[i] + nums[left] + nums[right] < 0:
                    right += 1
                else:
                    left -= 1
                
        return result

    # LeetCode
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     nums.sort()
    #     for i in range(len(nums)):
    #         if nums[i] > 0:
    #             break
    #         if i == 0 or nums[i - 1] != nums[i]:
    #             self.twoSumII(nums, i, res)
    #     return res

    # def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
    #     lo, hi = i + 1, len(nums) - 1
    #     while (lo < hi):
    #         sum = nums[i] + nums[lo] + nums[hi]
    #         if sum < 0:
    #             lo += 1
    #         elif sum > 0:
    #             hi -= 1
    #         else:
    #             res.append([nums[i], nums[lo], nums[hi]])
    #             lo += 1
    #             hi -= 1
    #             while lo < hi and nums[lo] == nums[lo - 1]:
    #                 lo += 1


input = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

solution = Solution()
print(solution.threeSum(input))