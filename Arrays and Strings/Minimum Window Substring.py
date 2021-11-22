# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def split_into_dict(word):
            char_dict = {}
            for char in word:
                if char in char_dict:
                    char_dict[char] = char_dict[char] + 1
                else:
                    char_dict[char] = 1
            return char_dict
        
        max_len = float('inf')
        result = ''
        for i in range(len(s)):
            t_list = split_into_dict(t)
            current_item = s[i]
            if current_item in t_list:
                # Check rest of 
                # print(s[i])
                
                # Dictionary update                
                t_list[s[i]] = t_list[s[i]] - 1
                if t_list[s[i]] == 0:
                    del t_list[s[i]]
                    
                if len(t_list) == 0:
                    if len(s[i:i + 1]) < max_len:
                        result = s[i:i + 1]
                        max_len = len(result)
                    
                for j in range(i + 1, len(s)):
                    
                    if s[j] in t_list:
                        # print(s[j])

                        # Dictionary update
                        t_list[s[j]] = t_list[s[j]] - 1
                        if t_list[s[j]] == 0:
                            del t_list[s[j]]
                            
                        if len(t_list) == 0:
                            if len(s[i:j + 1]) < max_len:
                                result = s[i:j + 1]
                                max_len = len(result)
                            break
        return result

    def minWindowTwoPointers(self, s: str, t: str) -> str:
        def string_contains(s, t):
            def split_into_dict(word):
                char_dict = {}
                for char in word:
                    if char in char_dict:
                        char_dict[char] = char_dict[char] + 1
                    else:
                        char_dict[char] = 1
                return char_dict
            
            dict_t = split_into_dict(t)
            for i in range(len(s)):
                if s[i] in dict_t:
                    dict_t[s[i]] = dict_t[s[i]] - 1
                    if dict_t[s[i]] == 0:
                        del dict_t[s[i]]
                    
            if len(dict_t) == 0:
                return True
            return False
        
        left = 0
        right = 1
        
        result = ""
        max_len = float('inf')
        while(right != len(s) + 1):
            if string_contains(s[left:right], t):
                if len(s[left:right]) < max_len:
                    result = s[left:right]
                    max_len = len(result)
                left += 1
            else:
                right += 1
                
        return result

solution = Solution()
solution.minWindow(s, t)