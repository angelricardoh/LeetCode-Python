# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def len(head):
            count = 0
            head_copy = head
            while head_copy != None:
                count += 1
                head_copy = head_copy.next
            return count
        
        def printList(head):
            head_copy = head
            while head_copy != None:
                print(head_copy.val, end=' ')
                head_copy = head_copy.next
            print()
        
        def invertList(head):
            current = head
            prev = None
            while current != None:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev
        
        if k == 1:
            return head
        
        # Find k.next position and save in temp
        original_head = copy.deepcopy(head)
        current = head
        result = head
        for i in range(k - 1):
            current = current.next
        temp = current.next
        current.next = None
        
        # Invert first k elements and fix k.next pointer
        new_head = invertList(result)
        
        current = new_head
        for i in range(k - 1):
            current = current.next
        current.next = temp        
        n = len(new_head)
        
        # For k and above
        result = new_head
        for j in range(k, n - k + 1, k):
            current_head = result
            previous_head = None
            
            # Reach j poition and store j - 1 pointer
            for _ in range(j):
                previous_head = current_head
                current_head = current_head.next
            
            previous_head.next = None
            current = current_head
            current_head_copy = current_head
            for i in range(k - 1):
                current = current.next
            
            if current is None:
                temp = None
            else:
                temp = current.next
                current.next = None

            # Invert j to j + k elements
            last_current = invertList(current_head_copy)
            previous_head.next = last_current
            current = last_current
            for i in range(k - 1):
                current = current.next
            if current is not None:
                current.next = temp
                        
        return result