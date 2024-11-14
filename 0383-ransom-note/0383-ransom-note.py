class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for element in ransomNote: 
            if element not in magazine:
                return False
            else:
                magazine = magazine.replace(element, "", 1)      
        return True