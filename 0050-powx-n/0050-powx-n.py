class Solution:
    def myPow(self, x: float, n: int) -> float:

        def calc_pow(x, n) :
            if x == 0 : 
                return 0
            if n == 0 :
                return 1

            res = calc_pow(x, n // 2)
            res = res * res

            if n % 2 == 1 :
                return res * x

            return res

        answer = calc_pow(x, abs(n))

        if n >= 0 :
            return answer
        
        return 1 / answer