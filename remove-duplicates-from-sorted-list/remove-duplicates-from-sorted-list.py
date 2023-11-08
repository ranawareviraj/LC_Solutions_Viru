# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node keeps pointer to the head
        dummy = ListNode(-101)
        dummy.next = head
        
        # Start curr at head and head at prev of head i.e dummy
        prev = dummy
        curr = head
        
        while curr != None:
            if curr.val != prev.val:
                prev.next = curr
                prev = curr
                curr = curr.next               
            else:
                curr = curr.next
                
        if prev != None:
            prev.next = None
        
        # By the end dummy.next will hold the ref to LL
        return dummy.next