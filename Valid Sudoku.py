# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check horizontally
        for i in range(len(board)):
            sanity_check_set = set()
            for j in range(len(board)):
                if board[i][j] == '.': 
                    continue
                if board[i][j] in sanity_check_set:
                    return False
                sanity_check_set.add(board[i][j])
                
        for i in range(len(board)):
            sanity_check_set = set()
            for j in range(len(board)):
                if board[j][i] == '.': 
                    continue
                if board[j][i] in sanity_check_set:
                    return False
                sanity_check_set.add(board[j][i])
                
        for slide_up in range(3):
            for slide_right in range(3):
                sanity_check_set = set()
                for i in range(3):
                    for j in range(3):
                        if board[i + (slide_up * 3)][j + (slide_right * 3)] == '.': 
                            continue
                        if board[i + (slide_up * 3)][j + (slide_right * 3)] in sanity_check_set:
                            return False
                        sanity_check_set.add(board[i + (slide_up * 3)][j + (slide_right * 3)])
                        
        return True