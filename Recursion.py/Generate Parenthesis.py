# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans

    def generateParenthesis(self, n: int) -> List[str]:
        def validateParenthesis(string):
            stack = 0
            for item in string:
                if item == '(':
                    stack += 1
                else:
                    if stack != 0:
                        stack -= 1
                    else:
                        return False
            if stack != 0:
                return False
            return True
        
        def backtrack(count_open, count_close, string, parenthesis_list):
            if count_open == 0 and count_close == 0:
                if validateParenthesis(string):
                    parenthesis_list.add(string)
                    # print(string)
                    return parenthesis_list
            
            left_list = set()
            right_list = set()
            if count_open != 0:
                left_list = backtrack(count_open - 1, count_close, string + '(', parenthesis_list)
            if count_close != 0:
                right_list = backtrack(count_open, count_close - 1, string + ')', parenthesis_list)
            return left_list.union(right_list)
            
        return backtrack(n, n, '', set())