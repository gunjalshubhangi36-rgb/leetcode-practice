class Solution(object):
    def longestCommonPrefix(self, strs):
        
        str2 = ""

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    
                    return str2

            str2 += strs[0][i]
                    
        return str2

        """
        :type strs: List[str]
        :rtype: str
        """
        