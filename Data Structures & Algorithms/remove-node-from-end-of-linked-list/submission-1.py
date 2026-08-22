# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def reversed(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None

            curr = node
            size = 0
            while curr:
                size += 1
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
        
            return prev
        
        curr = reversed(head)
        if curr is None:
            return None
        
        i = 1
        prev = None
        head = None
        while i<=n and curr:
            
            if i==n:
                if prev is None:
                    return reversed(curr.next)
                else:
                    prev.next  = curr.next
            else:
                if head is None:
                    head = curr
                prev = curr
            
            curr = curr.next
            i += 1

        return reversed(head)
            




            