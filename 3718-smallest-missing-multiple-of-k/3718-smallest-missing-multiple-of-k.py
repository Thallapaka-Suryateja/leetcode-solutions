class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=1
        while True:
            num=i*k
            if num not in nums:
                return num
            i+=1