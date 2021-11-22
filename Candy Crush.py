from typing import List

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        def print_board(board):
            for j in range(m):
                for i in range(n):
                    print(board[j][i], end='\t')
                print()

        def dfs(board, pos_y, pos_x, value, continuous_pos):
            m = len(board)
            n = len(board[0])
            
            if pos_y < 0 or pos_y >= m or pos_x < 0 or pos_x >= n:
                return
            
            # print(str(pos_y) + ' ' + str(pos_x))
            if board[pos_y][pos_x] == value and (pos_y, pos_x) not in continuous_pos:
                continuous_pos.append((pos_y, pos_x))
                
                dfs(board, pos_y + 1, pos_x, value, continuous_pos)
                dfs(board, pos_y - 1, pos_x, value, continuous_pos)
                dfs(board, pos_y, pos_x + 1, value, continuous_pos)
                dfs(board, pos_y, pos_x - 1, value, continuous_pos)

        def makeChanges(board, pos_y, pos_x):
            continuous_pos = []
            # dfs(board, 6, 2, board[6][2], continuous_pos)
            dfs(board, pos_y, pos_x, board[pos_y][pos_x], continuous_pos)

            # gather continous positions with 3 or more candies only
            continuous_pos_filtered = []
            for item in continuous_pos:
                if ((item[0], item[1] + 1) in continuous_pos and (item[0], item[1] - 1) in continuous_pos) or \
                    ((item[0], item[1] + 1) in continuous_pos and (item[0], item[1] + 2) in continuous_pos) or \
                    ((item[0], item[1] - 1) in continuous_pos and (item[0], item[1] - 2) in continuous_pos) or \
                    ((item[0] + 1, item[1]) in continuous_pos and (item[0] - 1, item[1]) in continuous_pos) or \
                    ((item[0] + 1, item[1]) in continuous_pos and (item[0] + 2, item[1]) in continuous_pos) or \
                    ((item[0] - 1, item[1]) in continuous_pos and (item[0] - 2, item[1]) in continuous_pos):
                    continuous_pos_filtered.append(item)

            if len(continuous_pos_filtered) < 3:
                return False
            # print(continuous_pos_filtered)

            # fill continuous positions with *
            for item in continuous_pos_filtered:
                board[item[0]][item[1]] = '*'
            # print_board(board)
                                
            # Reacommodate * spaces
            for local_i in range(n):
                count = 0
                end = 0
                for local_j in range(m):
                    if board[local_j][local_i] == '*':
                        count += 1
                        end = local_j
                
                l = 0
                for k in range(end, -1, -1):
                    # Is there a way to improve this block?
                    if l < m - count:
                        board[k][local_i] = board[k - count][local_i]
                        if k - count == -1:
                            board[k][local_i] = 0
                        else:
                            board[k][local_i] = board[k - count][local_i]
                    else:
                        board[k][local_i] = 0
                    l += 1
            return True

        m = len(board)
        n = len(board[0])

        changes = True
        while(changes):
            changes = False

            for j in range(m):
                if changes == True:
                    break
                for i in range(n):
                    if board[j][i] == 0:
                        continue

                    if makeChanges(board, j, i):
                        changes = True
                        break

        return board

board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
solution = Solution()
solution.candyCrush(board)