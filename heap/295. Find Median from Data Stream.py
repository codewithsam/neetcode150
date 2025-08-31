import heapq


class MedianFinder:

    def __init__(self):
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)

    def findMedian(self) -> float:
        n = len(self.min_heap)
        if n % 2 == 0:
            left_mid = int(n/2-0.5)
            right_mid = int(n/2+0.5)
            return (self.min_heap[left_mid] + self.min_heap[right_mid])/2
        else:
            mid = int(n/2)
            return float(self.min_heap[mid])


median_finder = MedianFinder()
median_finder.addNum(1)    # arr = [1]
median_finder.addNum(3)    # arr = [1, 2]
print(median_finder.findMedian()) # return 1.5 (i.e., (1 + 2) / 2)
median_finder.addNum(2)    # arr[1, 2, 3]
print(median_finder.findMedian()) # return 2.0