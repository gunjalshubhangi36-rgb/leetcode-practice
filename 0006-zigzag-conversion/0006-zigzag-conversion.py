class Solution(object):
    def convert(self, s, numRows):
        
        if numRows == 1:
            return s

        rows = [""] * numRows
        i = 0
        down = True

        for ch in s:
            rows[i] += ch

            if i == 0:
                down = True
            elif i == numRows - 1:
                down = False

            if down:
                i += 1
            else:
                i -= 1

        return "".join(rows)
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        