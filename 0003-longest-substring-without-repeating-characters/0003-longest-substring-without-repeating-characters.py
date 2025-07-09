class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = len(s)
        s_i, e_i = 0, 0
        result = 0

        if l <= 1:
            return l

        while e_i < l - 1 :
            alpb = set()

            for i in range(s_i, l):
                if s[i] in alpb:
                    break

                alpb.add(s[i])
                e_i = i

            result = max(result, len(alpb))
            s_i += 1

        return result

        