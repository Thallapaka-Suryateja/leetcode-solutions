class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = set()
        i = 0
        length = 0

        for k in range(len(s)):
            while s[k] in res:
                res.remove(s[i])
                i += 1

            res.add(s[k])
            length = max(length, k - i + 1)

        return length