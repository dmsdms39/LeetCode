class Solution:
    def isHappy(self, n: int) -> bool:
        next_nums = set()

        def get_next_number(n):
            output = 0

            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            return output
        
        while n not in next_nums:
            next_nums.add(n)
            n = get_next_number(n)
            if n == 1:
                return True
        
        return False

        