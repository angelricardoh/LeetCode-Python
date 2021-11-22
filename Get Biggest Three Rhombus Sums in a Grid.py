from typing import List
import heapq

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:    
        def getRombusSum(board, pos_x, pos_y, level):
            if level == 0:
                return board[pos_y][pos_x]
            
            m = len(board)
            n = len(board[0])
            sum = 0

            j = pos_y
            for i in range(pos_x - level, pos_x):
                if i < 0 or i >= n or j < 0 or j >= m:
                    return -1
                else:
                    sum += board[j][i] 
                j += 1

            j = pos_y + level
            for i in range(pos_x, pos_x + level):
                if i < 0 or i >= n or j < 0 or j >= m:
                    return -1
                else:
                    sum += board[j][i] 
                j -= 1

            j = pos_y
            for i in range(pos_x + level, pos_x, - 1):
                if i < 0 or i >= n or j < 0 or j >= m:
                    return -1
                else:
                    sum += board[j][i] 
                j -= 1

            j = pos_y - level
            for i in range(pos_x, pos_x - level, - 1):
                if i < 0 or i >= n or j < 0 or j >= m:
                    return -1
                else:
                    sum += board[j][i] 
                j += 1
            return sum

        rombus_sum_list = []
        heapq.heapify([])
        m = len(grid)
        n = len(grid[0])
        for y in range(0, m):
            for x in range(0, n):
                rombus_sum = 0
                level = 0
                while rombus_sum != -1:
                    rombus_sum = getRombusSum(grid, x, y, level)
                    if rombus_sum == -1:
                        continue
                    if len(rombus_sum_list) < 3 and rombus_sum not in rombus_sum_list:
                        heapq.heappush(rombus_sum_list, rombus_sum)
                    elif rombus_sum > rombus_sum_list[0] and rombus_sum not in rombus_sum_list:
                        heapq.heappop(rombus_sum_list)
                        heapq.heappush(rombus_sum_list, rombus_sum)
                        
                    level += 1

        if len(rombus_sum_list) == 1:
            return [heapq.heappop(rombus_sum_list)]
        elif len(rombus_sum_list) == 2:
            top_2 = heapq.heappop(rombus_sum_list)
            top = heapq.heappop(rombus_sum_list)
            return [top, top_2]
        else:
            top_3 = heapq.heappop(rombus_sum_list)
            top_2 = heapq.heappop(rombus_sum_list)
            top = heapq.heappop(rombus_sum_list)
        return [top, top_2, top_3]

# grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
# grid = [[7, 7, 7]]
grid = [[15,14,15,19,6,18,15,14],[18,7,8,10,3,5,11,19],[20,11,10,1,6,3,16,3],[7,14,4,9,18,14,13,3],[20,5,15,3,9,8,16,16],[6,7,4,12,2,19,11,20],[20,11,10,3,4,9,5,15],[13,10,4,18,16,2,4,20]]

solution = Solution()
print(solution.getBiggestThree(grid))