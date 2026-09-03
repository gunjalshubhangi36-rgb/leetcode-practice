class Solution(object):
    def reverse(self, x):
    

        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        x = str(abs(x))

        rev = int(x[::-1])

        
        rev = rev * sign
        

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
    
        return rev
        
        """
        :type x: int
        :rtype: int
        """
        