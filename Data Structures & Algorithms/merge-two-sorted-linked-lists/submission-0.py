# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = None
        while(list1 and list2):
            smaller = None
            first = False
            if(list1.val <= list2.val):
                smaller = list1
                first = True
            else:
                smaller = list2
            
            tmp = smaller.next
            smaller.next  = None
            if head is None:
                curr = smaller
                head = smaller
            
            curr.next = smaller
            curr = curr.next
            
            if first:
                list1 = tmp
            else:
                list2 = tmp
        
        if(list1):
            if curr:
                curr.next = list1
            else:
                head = list1
        if(list2):
            if curr:
                curr.next = list2
            else:
                head = list2
        return head
        

        