"""
LeetCode #121 — Best Time to Buy and Sell Stock
Difficulty: Easy
Topics: Array, Greedy, Sliding Window (conceptual intro)

Pattern — "running minimum + running max gain":
  Track the cheapest price seen so far (`min_price`).
  On every subsequent day, the best profit *if you sell today* is
  `price - min_price`.  Keep a rolling maximum of that quantity.

This is the conceptual bridge into sliding window: the "window" is
implicitly [day_of_min_price, today], and we slide the right end
forward one step at a time while the left end jumps to wherever
the minimum lives.

Time:  O(n)  — single pass
Space: O(1)  — two scalar variables
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """Return the maximum profit achievable from one buy-sell transaction.

    Args:
        prices: prices[i] is the stock price on day i.

    Returns:
        Maximum profit; 0 if no profitable trade exists.
    """
    min_price: float = float("inf")
    best_profit: int = 0

    for price in prices:
        if price < min_price:
            min_price = price                       # found a cheaper buy day
        elif price - min_price > best_profit:
            best_profit = price - min_price         # found a better sell day

    return best_profit


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------

def _test() -> None:
    # Standard example: buy day-1 (price 1), sell day-4 (price 6) → profit 5
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5

    # Prices only fall — no profitable trade
    assert max_profit([7, 6, 4, 3, 1]) == 0

    # Buy at 2, sell at 4
    assert max_profit([2, 4, 1]) == 2

    # Single price — nothing to sell
    assert max_profit([1]) == 0

    # All same prices
    assert max_profit([5, 5, 5, 5]) == 0

    # Min at last position — shouldn't be used (can't sell before buying)
    assert max_profit([3, 2, 6, 5, 0, 3]) == 4   # buy 2, sell 6

    print("All tests passed ✓")


if __name__ == "__main__":
    _test()
