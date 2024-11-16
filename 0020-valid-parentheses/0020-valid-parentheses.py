class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dic = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in bracket_dic:
                top = stack.pop() if stack else 0
                if bracket_dic[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack