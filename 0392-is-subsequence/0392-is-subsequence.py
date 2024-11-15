class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for char_t in t:
            if i == len(s):
                return True
            if s[i] == char_t :
                i += 1
            

        return False    

        