# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
# Example 4:

# Input: candidates = [1], target = 1
# Output: [[1]]
# Example 5:

# Input: candidates = [1], target = 2
# Output: [[1,1]]
 

# Constraints:

# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(candidates, target, current_list):
            for item in candidates:
                current_list.append(item)
                # print(current_list)

                sum = 0
                for element in current_list:
                    sum += element
                
                if sum < target:
                    # print(current_list)
                    backtrack(candidates, target, current_list)
                    current_list.pop()
                elif sum == target:
                    print(current_list)
                    element = current_list.copy()
                    element.sort()
                    if element not in result:
                        result.append(element)
                    current_list.pop()
                    # return
                else:
                    # print(current_list)
                    current_list.pop()
                    # return        
        backtrack(candidates, target, [])
        return result