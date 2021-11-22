# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified becase it contains only one word.
# Example 3:

# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]


import re 
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        string_array = []
        i = 0
        
        # Do distribution of words based on word length and concatenation and form sentences
        while len(words) != 0:
            current_string = ''
            length_reached = False
            while length_reached == False and len(words) != 0:
                current_word = words.pop(0)
                if len(current_string + current_word) < maxWidth:
                    current_string += current_word + ' '
                else:
                    length_reached = True
                
            current_string = current_string[:-1]
            string_array.append(current_string)
            
            if len(words) != 0:
                words.insert(0, current_word)
            else:
                while len(current_word) <= maxWidth - 1:
                    current_word += ' '
                string_array.append(current_word)    

        # iterate over sentences        
        result = [''] * len(string_array)
        for word_index in range(len(string_array)):
            spaces = 1
            current_string = ''
            while len(current_string) <= maxWidth:
                current_string = ''
                for char in string_array[word_index]:
                    if char == ' ':
                        new_space = "*" * spaces
                        current_string += new_space
                    else:
                        current_string += char

                # re.sub('*', ' ', current_string)
                if len(current_string) <= maxWidth:
                    result[word_index] = current_string
                
                spaces += 1
                
            current_string = result[word_index]
            
            # Fill sentences not evenly distributed starting from spapces from left to right it can match maxWidh
            if len(current_string) != maxWidth:
                aux_string = current_string
                add_index = 0
                for index_char in range(len(aux_string)):
                    char = aux_string[index_char]
                    
                    # Wrong logic, should find where each word ends and insert and empty space there not use spaces only
                    if char == '*':
                        current_string = current_string[:add_index] + '*' + current_string[add_index:]
                        if len(current_string) == maxWidth:
                            result[word_index] = current_string
                            break
                        # current_string.insert(add_index, = ' ')
                        add_index += 1
                    add_index += 1                        
        
        return result