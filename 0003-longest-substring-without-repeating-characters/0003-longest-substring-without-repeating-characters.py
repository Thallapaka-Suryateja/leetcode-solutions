class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        length=0
        i=0
        k=1
        j=len(s)
        res={s[i]}
        while k<j and i<j:
            if s[k] not in res:
                res.add(s[k])
                k+=1
            else:
                length1=k-i
                if length < length1:
                    length = length1
                i+=1
                k=i+1
                res={s[i]}
        if len(res)>length:
            length=len(res)
        return length
                