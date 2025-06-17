class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1 :
            return x

        start = 1
        end = x

        while start < end:
            
            val = (start + end) // 2
            
            sqrt = val * val

            if x == sqrt:
                return val
            elif x < sqrt:
                end = val
            elif start == val:
                break
            else:
                start = val

        
        return start