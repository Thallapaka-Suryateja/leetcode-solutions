class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i in strs:
            if i == "":
                return ""
            elif strs[0][0]!=i[0]:
                return ""
        s=""
        for j in range(len(strs[0])):
            for i in range(len(strs)):
                if j>=len(strs[i]):
                    return s
                if strs[0][j]!=strs[i][j]:
                    return s
                
            s=s+strs[0][j]
        return s
