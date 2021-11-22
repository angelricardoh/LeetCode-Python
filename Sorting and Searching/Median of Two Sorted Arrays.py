# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)). 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:

# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:

# Input: nums1 = [2], nums2 = []
# Output: 2.00000
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid = (len(nums1) + len(nums2)) // 2
        total_len = len(nums1) + len(nums2)
        arr = [0] * total_len
        
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr[k] = nums1[i]
                i += 1
            else:
                arr[k] = nums2[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(nums1):
            arr[k] = nums1[i]
            i += 1
            k += 1
 
        while j < len(nums2):
            arr[k] = nums2[j]
            j += 1
            k += 1
            
            
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        # if len(left_arr) == 0 or len(right_arr) == 0:
        #     return arr[mid]
        if len(right_arr) > len(left_arr):
            return right_arr[0]
        else:
            return (left_arr[len(left_arr) - 1] + right_arr[0]) / 2
        