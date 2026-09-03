class Solution(object):
    def myAtoi(self, s):

        s = s.strip()

        sign = 1

        if s.startswith("-"):
            sign = -1
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]

        num = 0

        for i in s:
            if i < "0" or i > "9":
                break
            num = num * 10 + int(i)

        num = num * sign

        if num > 2147483647:
            return 2147483647

        if num < -2147483648:
            return -2147483648
        
        return num
        """
        :type s: str
        :rtype: int
        """
        