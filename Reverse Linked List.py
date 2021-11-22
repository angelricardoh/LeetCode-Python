# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current_node = head
        list_nodes = []
        while current_node:
            if len(list_nodes) >= left - 1 and len(list_nodes) <= right - 1:
                list_nodes.insert(left - 1, current_node.val)
            else:
                list_nodes.append(current_node.val)
            current_node = current_node.next
            
            
        current_node = head
        index = 0
        while current_node:
            current_node.val = list_nodes[index]
            index += 1
            current_node = current_node.next
        return head

    # In place solution
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current_node = head
        list_nodes = []
        index = 1
        while current_node:
            if index >= left and index <= right:
                aux = current_node
                temp = current_node
                
                temp_val = current_node.val
                for i in range(left, right):
                    aux = aux.next
                    
                temp.val = aux.val
                aux.val = temp_val
                                
                left += 1
                right -= 1
                
            current_node = current_node.next
            index += 1
                
        return head

