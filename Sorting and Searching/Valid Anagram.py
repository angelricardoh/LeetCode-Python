# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}
        
        for char in s:
            if char in s_hashmap:
                s_hashmap[char] = s_hashmap[char] + 1
            else:
                s_hashmap[char] = 1
                
        for char in t:
            if char in t_hashmap:
                t_hashmap[char] = t_hashmap[char] + 1
            else:
                t_hashmap[char] = 1
        
        if len(s_hashmap) != len(t_hashmap):
            return False
        for item in s_hashmap:
            if item not in t_hashmap:
                return False
            if s_hashmap[item] != t_hashmap[item]:
                return False
        return True