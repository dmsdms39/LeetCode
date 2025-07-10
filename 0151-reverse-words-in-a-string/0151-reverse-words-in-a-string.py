class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split()
        return " ".join(reversed(slist))
