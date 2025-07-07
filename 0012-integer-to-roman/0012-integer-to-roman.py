class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        result = ""
        
        i = 0
        power = pow(10, i)

        while num >= power :
            one_symbol = numerals.get(power, "")
            five_symbol = numerals.get(5 * power, "")
            ten_symbol = numerals.get(10 * power, "")

            digit = num // power % 10

            i += 1
            power = pow(10, i)

            if digit == 9 :
                result = one_symbol + ten_symbol + result

            elif digit == 4 :
                result = one_symbol + five_symbol + result

            elif digit >= 5 :
                result = five_symbol + one_symbol * (digit - 5) + result

            else :
                result = one_symbol * digit + result


        return result

            