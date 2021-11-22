# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# Constraints:

#     1 <= nums.length <= 10
#     -10 <= nums[i] <= 10
#     All the numbers of nums are unique.

class Solution:  
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         self.solution = []
#         def backtrack(nums, num_list):
#             if len(nums) == 0:
#                 return num_list
            
#             for i in range(len(nums)):
#                 nums_copy = nums.copy()
#                 num_list_copy = num_list.copy()
#                 current = nums_copy.pop(i)
                
#                 num_list_copy.append(current)
#                 num_list_copy.sort()
#                 if num_list_copy not in self.solution:
#                     self.solution.append(num_list_copy)
#                 backtrack(nums_copy, num_list_copy)

#         backtrack(nums, [])
#         self.solution.append([])
#         return self.solution
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output