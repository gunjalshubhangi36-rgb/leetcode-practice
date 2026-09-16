class Solution(object):
    def isValid(self, s):
        stack = []

        for ch in s:

            if ch == "(":
                stack.append(")")
            
            elif ch == "{":
                stack.append("}")
            
            elif ch == "[":
                stack.append("]")
            
            else:

                if not stack:
                    return False
                
                if stack.pop() != ch:
                    return False
        return len(stack) == 0
        """
        :type s: str
        :rtype: bool
        """
        