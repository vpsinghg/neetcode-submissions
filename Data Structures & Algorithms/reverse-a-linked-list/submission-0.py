# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def recurse(head: Optional[ListNode]):
            if head == None:
                return None, None
            
            if head.next is None:
                return head, head

            curr = head
            
            rev_head, rev_end = recurse(curr.next)
            head.next = None
            rev_end.next = head
            return rev_head, head
        
        new_head, _ = recurse(head)
        return new_head



        