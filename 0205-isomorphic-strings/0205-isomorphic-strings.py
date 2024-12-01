from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if len(Counter(s)) != len(Counter(t)):
            return False

        def modifyStr(target):
            dic = {}
            result = ''

            for i in range(len(target)):
                result += dic.setdefault(target[i], str(i)+'.')

            return result

        s = modifyStr(s)
        t = modifyStr(t)

        return True if s == t else False
