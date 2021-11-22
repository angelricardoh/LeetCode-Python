# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:

# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"

# Constraints:

# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

class Solution:
    def decodeString(self, s: str) -> str:
        def getContent(s, global_mult = 1):
            result = ''
            current_string = ''
            stack = []
            current_mult = None
            for item in s:
                if item.isnumeric():
                    if current_string != '' and len(stack) == 0:
                        if current_mult is None:
                            result += current_string
                        else:
                            result += current_string * current_mult
                        current_string = ''
                    
                    if len(stack) != 0:
                        current_string += item
                    else:
                        if current_mult != None:
                            current_mult = (10 * current_mult) + int(item)
                        else:
                            current_mult = int(item)
                    
                    # if current string is not empty then add to result
                elif item == '[':
                    stack.append(item)
                    current_string += item
                elif item == ']':
                    stack.pop(0)
                    current_string += item
                    if len(stack) == 0:
                        result += getContent(current_string[1:-1], current_mult)
                        current_string = ''
                        current_mult = None
                else:
                    current_string += item 
                    
            # result += current_string
            if current_mult is None:
                result += current_string
            else:
                result += current_string * current_mult
            return result * global_mult    
        
        return getContent(s)