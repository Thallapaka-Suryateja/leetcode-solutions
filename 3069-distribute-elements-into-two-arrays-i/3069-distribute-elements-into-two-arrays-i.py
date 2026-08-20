class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for k in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[k])
            else:
                arr2.append(nums[k])

        return arr1 + arr2