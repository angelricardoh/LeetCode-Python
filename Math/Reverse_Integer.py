# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0
 

# Constraints:

# -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:    
        result = ''
        number_array = []
        number_string = str(x)
        print(number_string)
        for char in number_string:
            number_array.append(char)
        
        current_index = 0
        if number_array[0] == '-':
            current_index = 1
            number_array.pop(0)
            result = '-'
            
        # print(number_array[-1])
        while number_array[-1] == '0':
            if number_array == ['0']:
                break
            number_array.pop(-1)
        for i in range(len(number_array) - 1, -1, -1):
            # print(i)
            result += number_array[i]
            
        result = int(result)
        
        if result > 2147483648 - 1 or result < -2147483648:
            return 0
        
        return result