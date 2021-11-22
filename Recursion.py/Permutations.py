class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        def backtrack(nums, current_list):
            if len(nums) == 0:
                self.permutations.append(current_list)
                return current_list
            
            for num in nums:
                if num not in current_list:
                    nums_copy = nums.copy()
                    nums_copy.remove(num)
                    current_list_copy = current_list.copy()
                    current_list_copy.append(num)
                    backtrack(nums_copy, current_list_copy)
                        
        backtrack(nums, [])
        return self.permutations