from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # if len(Counter(s)) != len(Counter(t)):
        #     return False

        sDic, tDic = {}, {}

        for i in range(len(s)):
            if sDic.setdefault(s[i], i) != tDic.setdefault(t[i], i):
                return False

        return True
