class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letter = s.split(" ")
        letterDict = {}

        if len(letter) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            c = pattern[i]
            if c in letterDict.keys():
                if letterDict[c] != letter[i]:
                    return False
            else:
                letterDict[c] = letter[i]
            
            if letter[i]+"_" in letterDict.keys():
                if letterDict[letter[i]+"_"] != c:
                    return False
            else:
                letterDict[letter[i]+"_"] = c

        
        return True