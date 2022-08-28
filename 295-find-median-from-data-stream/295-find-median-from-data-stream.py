import heapq
class MedianFinder:

    def __init__(self):
        self.min = []
        self.max = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max, -num)
        heapq.heappush(self.min, -heapq.heappop(self.max))
        if len(self.min)>len(self.max):
            heapq.heappush(self.max, -heapq.heappop(self.min))

    def findMedian(self) -> float:
        if len(self.max)==len(self.min):
            return (self.min[0]-self.max[0])/2
        else:
            return -self.max[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()