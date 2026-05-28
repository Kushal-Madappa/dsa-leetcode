# LeetCode: Isomorphic Strings (#205)
# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for cs, ct in zip(s, t):
            mapped = s_to_t.get(cs)
            if mapped is None:
                if ct in t_to_s:
                    return False
                s_to_t[cs] = ct
                t_to_s[ct] = cs
            elif mapped != ct:
                return False
        return True
