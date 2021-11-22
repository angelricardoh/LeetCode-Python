# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true
 
# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.insert(0, char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    current_item = stack.pop(0)
                    if current_item == '(' and char == ')':
                        continue
                    elif current_item == '[' and char == ']':
                        continue
                    elif current_item == '{' and char == '}':
                        continue
                    else:
                        return False
        if len(stack) != 0:
            return False
        return True
        