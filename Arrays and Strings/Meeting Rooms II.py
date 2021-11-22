# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key=lambda x:x[1])
        intervals.sort(key=lambda x:x[0])
        
        groups = []
        for item in intervals:
            
            no_group = True
            for group in groups:
                n = len(group)
                if group[n - 1][1] <= item[0]:
                    no_group = False
                    group.append(item)
                    break
                    
            if no_group:
                groups.append([item])
                    
        return len(groups)