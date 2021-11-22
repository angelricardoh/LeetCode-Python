# Given an array of unique strings words, return all the word squares you can build from words. The same word from words can be used multiple times. You can return the answer in any order.

# A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).

# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

# Example 1:

# Input: words = ["area","lead","wall","lady","ball"]
# Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# Example 2:

# Input: words = ["abat","baba","atan","atal"]
# Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def checkSquares(list_of_words):
            n = len(list_of_words)
            for i in range(n):
                for j in range(n):
                    if list_of_words[i][j] == list_of_words[j][i]:
                        continue
                    else:
                        return False
                    
            return True
        
        result = []
        def backtracking(list_of_words, words):
            if len(list_of_words) >= 1:
                if len(list_of_words) == len(list_of_words[0]):
                    if checkSquares(list_of_words):
                        result.append(list_of_words)
                elif len(list_of_words) > len(list_of_words[0]):
                    return
                        
            for word in words:
                list_of_words_copy = list_of_words.copy()
                list_of_words_copy.append(word)
                backtracking(list_of_words_copy, words)
                
        backtracking([], words)
        return result

    def backtracking(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()

    def buildPrefixHashTable(self, words):
        self.prefixHashTable = {}
        for word in words:
            for prefix in (word[:i] for i in range(1, len(word))):
                self.prefixHashTable.setdefault(prefix, set()).add(word)

    def getWordsWithPrefix(self, prefix):
        if prefix in self.prefixHashTable:
            return self.prefixHashTable[prefix]
        else:
            return set([])
        
    def wordSquaresLeetCode(self, words: List[str]) -> List[List[str]]:

        self.words = words
        self.N = len(words[0])
        self.buildPrefixHashTable(self.words)

        results = []
        word_squares = []
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results