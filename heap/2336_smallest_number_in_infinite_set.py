# LeetCode: Smallest Number in Infinite Set (#2336)
# https://leetcode.com/problems/smallest-number-in-infinite-set/
import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.next_val = 1
        self.added_back = []
        self.in_heap = set()

    def popSmallest(self) -> int:
        if self.added_back:
            val = heapq.heappop(self.added_back)
            self.in_heap.discard(val)
            return val
        val = self.next_val
        self.next_val += 1
        return val

    def addBack(self, num: int) -> None:
        if num < self.next_val and num not in self.in_heap:
            heapq.heappush(self.added_back, num)
            self.in_heap.add(num)
