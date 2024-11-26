from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_freq = [0] * 26
        t_freq = [0] * 26
        
        for i in range(len(s)):
            s_freq[ord(s[i]) - ord('a')] += 1
            t_freq[ord(t[i]) - ord('a')] += 1

        if any(s_freq[i] != t_freq[i] for i in range(0, 26)):
            return False
        
        return True

