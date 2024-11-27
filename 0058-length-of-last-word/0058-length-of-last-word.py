class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        isEnd = False
        cnt = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if isEnd:
                    return cnt
            else:
                isEnd = True
                cnt += 1
        
        return cnt