# LeetCode: Online Stock Span (#901)
# https://leetcode.com/problems/online-stock-span/


class StockSpanner:

    def __init__(self):
        # Each element is [price, span]. Monotonic decreasing stack by price.
        self.stack: list[list[int]] = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append([price, span])
        return span
