class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def recurse(head):
            if head is None or head.next is None:
                return head

            new_head = recurse(head.next)

            head.next.next = head
            head.next = None

            return new_head

        return recurse(head)