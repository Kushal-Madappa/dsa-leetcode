# LeetCode: Search Suggestions System (#1268)
# https://leetcode.com/problems/search-suggestions-system/
from bisect import bisect_left
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""
        lo = 0
        for ch in searchWord:
            prefix += ch
            lo = bisect_left(products, prefix, lo)
            suggestions = []
            for i in range(lo, min(lo + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break
            result.append(suggestions)
        return result
