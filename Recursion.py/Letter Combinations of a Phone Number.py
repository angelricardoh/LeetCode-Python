# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

mapping = [[''], [''], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], \
                  ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(combination_list, digits):

            new_combination_list = []
            if len(digits) > 0:

                current_digit = digits.pop(0)
                current_index = int(current_digit)

                if len(combination_list) != 0:
                    for item in combination_list:
                        for mapped_char in mapping[current_index]:
                            new_combination_list.append(item + mapped_char)
                else:
                    for mapped_char in mapping[current_index]:
                        new_combination_list.append(mapped_char)

                new_combination_list = backtrack(new_combination_list, digits)
                return new_combination_list

            return combination_list
        
        digits_list = []
        for digit in digits:
            digits_list.append(digit)    
        result = ""
        if len(digits_list) > 0:

            result = backtrack([], digits_list)
            
        return result