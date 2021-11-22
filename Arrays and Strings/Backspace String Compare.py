# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a##c", t = "#a#c"
# Output: true
# Explanation: Both s and t become "c".
# Example 4:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def trimString(s):
            i = 0
            while True:
                if i >= len(s):
                    break
                aux = s[i]
                if aux == '#' and i == 0:
                    s = s[i + 1:]
                    i = 0
                elif aux == '#':
                    s = s[:i - 1] + s[i + 1:]
                    i -= 1
                else:
                    i += 1
            return s
                    
        s = trimString(s)
        t = trimString(t)
                
        if s == t:
            return True
        return False