import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        arr = []

        for stone in stones:
            heapq.heappush(arr,-stone)
        
        while(len(arr)>0):
            if len(arr) == 1:
                return -1*arr[0]
            first = -1 * heapq.heappop(arr)
            second = -1 * heapq.heappop(arr)

            if first != second:
                heapq.heappush(arr,second-first)
        
        return 0
        



        