# Given a string num which represents an integer, return true if num is a strobogrammatic number.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Example 1:

# Input: num = "69"
# Output: true
# Example 2:

# Input: num = "88"
# Output: true
# Example 3:

# Input: num = "962"
# Output: false
# Example 4:

# Input: num = "1"
# Output: true

# Constraints:

# 1 <= num.length <= 50
# num consists of only digits.
# num does not contain any leading zeros except for zero itself.

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        def backtracking(num, left, right):
            if right < left:
                return True
            
            k = right - left + 1
            if k >= 2:
                if num[left] == '6' and num[right] == '9':
                    return backtracking(num, left + 1, right - 1)
                elif num[left] == '9' and num[left] == '6':
                    return backtracking(num, left + 1, right - 1)
                elif num[left] == '1' and num[right] == '1':
                    return backtracking(num, left + 1, right - 1)
                elif num[left] == '8' and num[right] == '8':
                    return backtracking(num, left + 1, right - 1)
                elif num[left] == '0' and num[right] == '0':
                    return backtracking(num, left + 1, right - 1)
                else:
                    return False
            else:
                if num[left] == '1':
                    return True
                elif num[left] == '8':
                    return True
                elif num[left] == '0':
                    return True
                
            backtracking(num, 0, len(num) - 1)