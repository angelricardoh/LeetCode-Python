# Definition for singly-linked list.
import copy
class ListNode:
    def __init__(self, val=0, next=None, previous=None):
        self.val = val
        self.next = next
        self.previous = None
        
class Solution:    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Efficient and simple solution
        str_l1 = ''
        str_l2 = ''
        
        while l1 is not None:
            str_l1 += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            str_l2 += str(l2.val)
            l2 = l2.next
            
        result = int(str_l1) + int(str_l2)
        result_str = str(result)
        
        result_node = ListNode(val = 0)
        result_head = result_node
        for i in range(len(result_str)):
            result_node.val = result_str[i]
            if i != len(result_str) - 1:
                result_node.next = ListNode()
            result_node = result_node.next

        return result_head 

        # def invertList(head):
        #     current = head
        #     prev = None
        #     while current != None:
        # next = current.next
        # current.next = prev
        # prev = current
        # current = next
        #     return prev
        # l1_copy = copy.copy(l1)
        # l2_copy = copy.copy(l2)

        # l1_copy = invertList(l1_copy)
        # l2_copy = invertList(l2_copy)
        
        # result = ListNode(val = 0)
        # result_head = result
        # while l1_copy is not None and l2_copy is not None:
        #     sum = l1_copy.val + l2_copy.val
        #     if sum >= 10:
        #         result.val += sum % 10
        #         if result.next is None:
        #     result.next = ListNode(val = 1)
        #     else:
        #         result.val += sum
        #     l1_copy = l1_copy.next
        #     l2_copy = l2_copy.next
        #     if result.next is None and (l1_copy or l2_copy):
        #         result.next = ListNode(val = 0)
        #     result = result.next
            
        # while l1_copy is not None:
        #     sum = result.val + l1_copy.val
            
        #     if sum >= 10:
        #         result.val = sum % 10
        #         if result.next is None:
        #     result.next = ListNode(val = 1)
        #     else:
        #         result.val = sum % 10
            
        #     l1_copy = l1_copy.next
        #     if result.next is None and l1_copy:
        #         result.next = ListNode(val = 0)
        #     result = result.next
            
        # while l2_copy is not None:
        #     sum = result.val + l2_copy.val
            
        #     if sum >= 10:
        #         result.val = sum % 10
        #         if result.next is None:
        #     result.next = ListNode(val = 1)
        #     else:
        #         result.val = sum % 10
            
        #     l2_copy = l2_copy.next  
        #     if result.next is None and l2_copy:
        #         result.next = ListNode(val = 0)
        #     result = result.next  