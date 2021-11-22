# Given a string s, return the length of the longest substring that contains at most two distinct characters.

 

# Example 1:

# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.
# Example 2:

# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of English letters.


class Solution:    
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        def differentCharFromEnd(s: str):
            n = len(s)

            prev = s[n - 1]
            for i in range(n - 2, -1 , -1):
                if s[i] != prev:
                    return s[i]
                
        hash_char = {}
        n = len(s)
        right = 0
        left = 0
        result = ''
        
        while right < n:
            hash_char[s[right]] = right
            
            if len(hash_char) > 2:
                current_string = s[left: right]
                # print(current_string)
                if len(current_string) > len(result):
                    result = current_string
                char  = differentCharFromEnd(s[left: right])
                left = hash_char[char] + 1
                del hash_char[char]
                
            right += 1

        # Check last substring
        current_string = s[left: right]
        if len(current_string) > len(result):
            result = current_string
            
        return len(result)