class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        result = 0
        alpb = set()

        if len(s) <= 1:
            return len(s)

        for right in range(len(s)):

            while s[right] in alpb:
                alpb.remove(s[left])
                left += 1
            
            alpb.add(s[right])
            result = max(result, len(alpb))

        return result

        