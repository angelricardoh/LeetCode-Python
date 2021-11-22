# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

# Example 1:

# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: true
# Explanation: We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# Example 2:

# Input: start = "X", end = "L"
# Output: false
# Example 3:

# Input: start = "LLR", end = "RRL"
# Output: false
# Example 4:

# Input: start = "XL", end = "LX"
# Output: true
# Example 5:

# Input: start = "XLLR", end = "LXLX"
# Output: false

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        result = ''
        
        i = 0
        while i < n - 1:
            if start[i:i+2] == end[i:i+2]:
                result += end[i]
                result += end[i + 1]
                i += 2
            elif start[i:i+2][::-1] == end[i:i+2] and (end[i:i+2] == 'LX' or end[i:i+2] == 'XR'):
                result += end[i]
                result += end[i + 1]
                i += 2
            else:
                result += start[i]
                i += 1
                
        if result == end:
            return True
        return False
    
    def canTransformLeetCode(self, start: str, end: str) -> bool:
        if len(start) != len(end): return False
        
        # check L R orders are the same
        if start.replace('X','') != end.replace('X', ''): return False
        
        n = len(start)
        Lstart = [i for i in range(n) if start[i] == 'L']
        Lend = [i for i in range(n) if end[i] == 'L']
        
        Rstart = [i for i in range(n) if start[i] == 'R']
        Rend = [i for i in range(n) if end[i] == 'R']
		# check L positions are correct
        for i, j in zip(Lstart, Lend):
            if i < j:
                return False
            
        # check R positions are correct
        for i, j in zip(Rstart, Rend):
            if i > j:
                return False
            
        return True