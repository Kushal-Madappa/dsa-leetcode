# LeetCode: Integer to Roman (#12)
# https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:
        pairs = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
        ]
        out = []
        for value, symbol in pairs:
            while num >= value:
                out.append(symbol)
                num -= value
        return "".join(out)
