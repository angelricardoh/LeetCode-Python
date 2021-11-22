# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        i = 0
        invalid = False
        while not invalid:


            prefix_set = set()
            for item in strs:
                if i >= len(item):
                    invalid = True
                    break
                    
                prefix_set.add(item[0:i + 1])
            if len(prefix_set) == 1:
                i += 1
                result = item[0:i]
                # print(result)
            else:
                invalid = True
                break
                
        return result