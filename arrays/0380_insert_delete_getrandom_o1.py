# LeetCode: Insert Delete GetRandom O(1) (#380)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
import random


class RandomizedSet:

    def __init__(self):
        self.values = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        idx = self.index[val]
        last = self.values[-1]
        self.values[idx] = last
        self.index[last] = idx
        self.values.pop()
        del self.index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
