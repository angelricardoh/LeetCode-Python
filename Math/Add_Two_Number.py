# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0

        result = ListNode(val=0)
        initial = result
        
        while l1 != None or l2 != None:
            sum = 0
            if l1 == None:
                sum = l2.val
                l2 = l2.next
            elif l2 == None:
                sum = l1.val
                l1 = l1.next
            else:
                sum = (l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next
            
            if l1 != None or l2 != None or sum >= 10 or result.val + sum >= 10:
                result.next = ListNode(val=0)
            
            if sum >= 10:
                result.val += sum % 10
                result.next.val += 1
            elif result.val + sum >= 10:
                result.val = 0
                result.next.val += 1
            else:
                result.val += sum
            
            result = result.next

        return initial