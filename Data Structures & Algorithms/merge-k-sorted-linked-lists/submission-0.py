# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        min_heap = []

        for i,node in enumerate(lists):
            if node is None:
                continue
            min_heap.append((node.val,i))
            lists[i] = node.next
        
        if len(min_heap) ==0:
            return None
        heapq.heapify(min_heap)

        head = None
        curr = None

        while(len(min_heap)):
            val, i = heapq.heappop(min_heap)
            node = ListNode(val)
            if head is None:
                head = node
                curr = node
            else:
                curr.next = node
                curr = node
            
            if lists[i] is not None:
                heapq.heappush(min_heap,(lists[i].val,i))
                lists[i] = lists[i].next
        
        return head
        

            




        

        
