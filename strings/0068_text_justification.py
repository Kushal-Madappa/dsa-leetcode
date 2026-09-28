# LeetCode: Text Justification (#68)
# https://leetcode.com/problems/text-justification/
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i, n = 0, len(words)
        while i < n:
            # Greedy: pack as many words as fit (with 1 space between each)
            j = i
            line_len = 0
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1
            gaps = j - i - 1
            is_last = (j == n)
            if gaps == 0 or is_last:
                # Left-justify: single spaces, pad end
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - line_len
                base, extra = divmod(total_spaces, gaps)
                parts = []
                for k in range(i, j - 1):
                    parts.append(words[k])
                    parts.append(" " * (base + (1 if (k - i) < extra else 0)))
                parts.append(words[j - 1])
                line = "".join(parts)
            result.append(line)
            i = j
        return result
