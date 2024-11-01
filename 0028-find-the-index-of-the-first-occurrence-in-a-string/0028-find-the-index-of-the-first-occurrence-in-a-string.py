class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        haylength = len(haystack)
        needlelength = len(needle)

        for i in range(haylength - needlelength+1):
            if haystack[i:i + needlelength] == needle:
                return i
            
        return -1
        
        