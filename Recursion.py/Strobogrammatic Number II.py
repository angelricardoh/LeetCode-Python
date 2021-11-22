# Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Example 1:

# Input: n = 2
# Output: ["11","69","88","96"]
# Example 2:

# Input: n = 1
# Output: ["0","1","8"]
 
# Constraints:

# 1 <= n <= 14

import copy

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def recursive(word, left, right, listing):
            k = right - left + 1
            if k <= 0:
                listing.append(word)
                return listing
            elif k  >= 2:
                word = copy.deepcopy(word)
                word[left] = '1'
                word[right] = '1'
                listing = recursive(word, left + 1, right - 1, listing)
                word = copy.deepcopy(word)
                word[left] = '8'
                word[right] = '8'
                listing = recursive(word, left + 1, right - 1, listing)
                word = copy.deepcopy(word)
                word[left] = '0'
                word[right] = '0'
                listing = recursive(word, left + 1, right - 1, listing)
                word = copy.deepcopy(word)
                word[left] = '6'
                word[right] = '9'
                listing = recursive(word, left + 1, right - 1, listing)
                word = copy.deepcopy(word)
                word[left] = '9'
                word[right] = '6'
                listing = recursive(word, left + 1, right - 1, listing)
            elif k == 1:
                # Can be either left or right
                word[left] = '1'
                word = copy.deepcopy(word)
                listing.append(word)
                word = copy.deepcopy(word)
                word[left] = '8'
                listing.append(word)
                word = copy.deepcopy(word)
                word[left] = '0'
                listing.append(word)
                
            return listing
            
        word = [' '] * n
        listing = recursive(word, 0, n - 1, [])
        result = set()
        for string in listing:
            if n <= 1 or string[0] != '0':
                result.add("".join(string)) 

        return result
            