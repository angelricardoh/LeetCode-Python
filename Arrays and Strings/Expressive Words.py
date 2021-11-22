# Sometimes people repeat letters to represent extra feeling. For example:

# "hello" -> "heeellooo"
# "hi" -> "hiiii"
# In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

# You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
# Return the number of query strings that are stretchy.

# Example 1:

# Input: s = "heeellooo", words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
# Example 2:

# Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
# Output: 3
 
# Constraints:

# 1 <= s.length, words.length <= 100
# 1 <= words[i].length <= 100
# s and words[i] consist of lowercase letters.

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        list_s = []
        current_char = ''
        index = -1
        for item in s:
            if item != current_char:
                index += 1
                current_char = item
                list_s.append((item, 1))
            else:
                list_s[index] = (item, list_s[index][1] + 1)
                
        result = 0
        for word in words:
            list_word = []
            index = -1
            current_char = ''
            for item in word:
                if item != current_char:
                    index += 1
                    current_char = item
                    list_word.append((item, 1))
                else:
                    list_word[index] = (item, list_word[index][1] + 1)
            
            stretchy = True
            if len(list_word) != len(list_s) or len(list_word) > len(list_s):
                continue
                
            for index in range(len(list_word)):
                if list_word[index][0] != list_s[index][0]:
                    stretchy = False
                    break
                else:
                    if list_s[index][1] == list_word[index][1] or \
                        list_s[index][1] >= list_word[index][1] + 2 or \
                        (list_word[index][1] >= 2 and list_s[index][1] >= list_word[index][1] + 1):
                        continue
                    else:
                        stretchy = False
                        break
                        
            if stretchy:
                result += 1
                
        return result