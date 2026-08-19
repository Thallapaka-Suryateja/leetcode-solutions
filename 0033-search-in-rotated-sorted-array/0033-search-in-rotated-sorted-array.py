class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binsearch(low,high,nums,target):
            while(low<=high):
                mid = low + (high-low)//2
                
                if nums[mid] == target:
                    return mid
                if nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return -1

        i=1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                break
            i+=1
        
        idx1=binsearch(0,i-1,nums,target)
        idx2=binsearch(i,len(nums)-1,nums,target)
        if idx1 == -1 and idx2 == -1:
            return -1
        elif idx1 == -1:
            return idx2
        else:
            return idx1
