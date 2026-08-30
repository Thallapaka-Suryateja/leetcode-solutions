class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        min_idx = max_idx = 0

        for i in range(n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i

        left = max(min_idx, max_idx) + 1
        right = n - min(min_idx, max_idx)
        both = min(min_idx, max_idx) + 1 + n - max(min_idx, max_idx)

        return min(left, right, both)