class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max1=0
        min1=100000000
        for i in range(len(nums)):
            max1=max(max1,nums[i])
            min1 = 1000000000
            for j in range(i,len(nums)):
                min1 = min(min1,nums[j])
            if (max1 - min1) <= k:
                return i
        return -1