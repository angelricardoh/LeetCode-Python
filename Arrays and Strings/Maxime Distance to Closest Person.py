# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

# Return that maximum distance to the closest person.

# Example 1:

# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:

# Input: seats = [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Example 3:

# Input: seats = [0,1]
# Output: 1

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_length = 0
        zero_count = 0
        n = len(seats)
        starts_zero = True if seats[0] == 0 else False
        
        for item in seats:
            if item == 0:
                zero_count += 1
            elif item == 1:
                if starts_zero == True:
                    max_length = zero_count
                    starts_zero = False  
                elif ceil(zero_count / 2) > max_length:
                    max_length = ceil(zero_count / 2)
                zero_count = 0
        
        if seats[n - 1] == 0 and zero_count > max_length:
            return zero_count
        return max_length