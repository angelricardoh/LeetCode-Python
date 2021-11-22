# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:

# Input: head = [1], n = 1
# Output: []

# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Constraints:

#     The number of nodes in the list is sz.
#     1 <= sz <= 30
#     0 <= Node.val <= 100
#     1 <= n <= sz

# Follow up: Could you do this in one pass?

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def nodeCount(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count
        
        if nodeCount(head) == 1:
            head.val = ''
            return head
        
        m = nodeCount(head) - n
        
        result = head
        prev = None
        for _ in range(m):
            prev = head
            head = head.next
            
        if prev:
            prev.next = head.next
        else:
            result = head.next
        return result