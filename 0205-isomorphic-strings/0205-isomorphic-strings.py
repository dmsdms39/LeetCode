from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if len(Counter(s)) != len(Counter(t)):
            return False

        sDic = {}
        tDic = {}

        for i in range(len(s)):
            sIdx = sDic.setdefault(s[i], i)
            tIdx = tDic.setdefault(t[i], i)

            if sIdx != tIdx:
                return False

        return True
