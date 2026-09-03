class Solution(object):
    def isMatch(self, s, p):

        memo = {}

        def match(s, p):
            if (s, p) in memo:
                return memo[(s, p)]

            if not p:
                return not s

            first = bool(s) and (s[0] == p[0] or p[0] == '.')

            if len(p) >= 2 and p[1] == '*':
                ans = match(s, p[2:]) or (first and match(s[1:], p))
            else:
                ans = first and match(s[1:], p[1:])

            memo[(s, p)] = ans
            return ans

        return match(s, p)


        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        