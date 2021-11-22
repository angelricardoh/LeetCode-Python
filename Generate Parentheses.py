# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
# All combinations
#         def validateParenthesis(string):
#             stack = []
#             for item in string:
#                 if item == '(':
#                     stack.append('(')
#                 if item == ')':
#                     if len(stack) == 0:
#                         return False
#                     else:
#                         stack.pop()
                        
#             if len(stack) == 0:
#                 return True
#         list_strings = ['(', ')']
#         for i in range(1, n * 2):
#             new_list_strings = []
#             for item in list_strings:
#                 if validateParenthesis(item + '('):
#                     new_list_strings.append(item + '(')
#                 if validateParenthesis(item + '('):
#                     new_list_strings.append(item + '(')
#             list_strings = new_list_strings
            
#         result = []
#         for item in list_strings:
#             if validateParenthesis(item):
#                 result.append(item)
                
#         return new_list_strings
    
# Backtracking
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