# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        head = None
        curr = None

        while list1 and list2:
            if list1.val <= list2.val:
                smaller = list1
                list1 = list1.next
            else:
                smaller = list2
                list2 = list2.next

            if head is None:
                head = smaller
                curr = smaller
            else:
                curr.next = smaller
                curr = smaller

        if list1:
            if curr:
                curr.next = list1
            else:
                head = list1

        if list2:
            if curr:
                curr.next = list2
            else:
                head = list2

        return head        