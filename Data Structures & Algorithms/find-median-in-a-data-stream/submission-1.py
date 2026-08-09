
class MedianFinder:
    def __init__(self):
        self.median_pos = -1
        self.size = 0
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.stream.sort()
        self.size += 1

        if (self.size % 2) == 1:
            self.median_pos += 1

    def findMedian(self) -> float:
        first = self.stream[self.median_pos]
        if self.size % 2 == 0:
            second = self.stream[self.median_pos + 1]

            return (first + second) / 2
        return first
