class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = max(min_idx, max_idx) + 1
        right = n - min(min_idx, max_idx)

        both = min(min_idx, max_idx) + 1 + n - max(min_idx, max_idx)

        return min(left, right, both)