class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if i == len(s):
            return True
        for char_t in t:
            if s[i] == char_t :
                i += 1
            if i == len(s):
                return True

        return False    

        