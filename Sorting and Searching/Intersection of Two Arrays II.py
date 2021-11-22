# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 
# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        result = []
        
        curr1 = nums1.pop(0)
        curr2 = nums2.pop(0)
        
        # while pointer1 < len(nums1) and pointer2 < len(num2):
        while curr1 is not None and curr2 is not None:
            if curr1 == curr2:
                result.append(curr1)
                if len(nums1) == 0:
                    curr1 = None
                    continue
                if len(nums2) == 0:
                    curr2 = None
                    continue
                
                curr1 = nums1.pop(0)
                curr2 = nums2.pop(0)

            elif curr1 < curr2:
                if len(nums1) == 0:
                    curr1 = None
                else:   
                    curr1 = nums1.pop(0)
            else:
                if len(nums2) == 0:
                    curr2 = None
                else:
                    curr2 = nums2.pop(0)
    
        return result