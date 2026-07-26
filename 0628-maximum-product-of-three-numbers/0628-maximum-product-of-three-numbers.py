class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        first = second = third = float('-inf')
        small1 = small2 = float('inf')

        for num in nums:

            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num

            if num < small1:
                small2 = small1
                small1 = num
            elif num < small2:
                small2 = num

        return max(first * second * third,
                   first * small1 * small2)
        