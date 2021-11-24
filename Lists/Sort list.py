# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_list = []
        head_copy = head
        while head_copy:
            head_list.append(head_copy.val)
            head_copy = head_copy.next
        
        head_list.sort()
        result = head
        while head_list:
            current = head_list.pop(0)
            head.val = current
            head  = head.next
        return result