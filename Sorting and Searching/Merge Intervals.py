# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        result = []
        n = len(intervals)
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        
        upper_bound = -1
        for i in range(n):
            current_range = intervals[i]
            if intervals[i][1] <= upper_bound:
                continue
                
            for j in range(i + 1, n):
                min_range = -1
                max_range = -1
                if current_range[1] >= intervals[j][0]:
                    min_range = min(current_range[0], intervals[j][0])
                    max_range = max(current_range[1], intervals[j][1])
                    current_range = [min_range, max_range]
                    if max_range > upper_bound:
                        upper_bound = max_range
                        
            result.append(current_range)

        if intervals[i - 1][1] < intervals[i][0] and intervals[i][1] > upper_bound and intervals[i] not in result:
            result.append(intervals[i])
                    
        return result
        