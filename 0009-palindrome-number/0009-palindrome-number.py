class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        
        if x < 10 :
            return True

        x = str(x)

        left_idx = 0      
        right_idx = len(x) - 1

        while left_idx < right_idx :
            if x[left_idx] != x[right_idx] :
                return False
            left_idx += 1
            right_idx -= 1

        return True