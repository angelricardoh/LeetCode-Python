class Solution:
    def intToRoman(self, num: int) -> str:
        def getDigit(res, pref, inf, suf):
            string_res = ""
            if res == 1:
                string_res += pref
            if res == 2:
                string_res += pref + pref
            if res == 3:
                string_res += pref + pref + pref
            if res == 4:
                string_res += pref + inf
            if res == 5:
                string_res += inf
            if res == 6:
                string_res +=  inf + pref
            if res == 7:
                string_res += inf + pref + pref
            if res == 8:
                string_res += inf + pref + pref + pref
            if res == 9:
                string_res += pref + suf
            return string_res

        string_result = ""
        res = int(num / 1000)
        if res > 0:
            digit = getDigit(res, 'M', '-', '-')
            string_result += digit
            num -= 1000 * res
        res = int(num / 100)
        if res > 0:
            digit = getDigit(res, 'C', 'D', 'M')
            string_result += digit
            num -= 100 * res
        res = int(num / 10)
        if res > 0:
            digit = getDigit(res, 'X', 'L', 'C')
            string_result += digit
            num -= (10 * res)
        res = int(num / 1)
        if res > 0:
            digit = getDigit(res, 'I', 'V', 'X')
            string_result += digit
        return string_result