import heapq

class MedianFinder:

    def __init__(self):
        self.left = [] # stores lower half managed by max heap
        self.right = [] # right half managed by mean heap


    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush(self.left, -num)
            return
        
        # if num is smaller than max in the lower half then insert to lower half
        if num <= -1*self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        # rebalance
        if len(self.left) > (len(self.right)+1):
            heapq.heappush(self.right, -1*heapq.heappop(self.left))
        elif(len(self.right) > len(self.left)):
            heapq.heappush(self.left, -1*heapq.heappop(self.right))
        

        

    def findMedian(self) -> float:
        if(len(self.left)>len(self.right)):
            return -self.left[0]
        
        return (-self.left[0] + self.right[0])/2
        
        