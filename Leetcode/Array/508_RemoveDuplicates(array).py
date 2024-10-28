'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements should be
 kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the 
following things:

Change the array nums such that the first k elements of nums contain the unique elements in
 the order they were present in nums initially. The remaining elements of nums are not
 important as well as the size of nums.
Return k.'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 0
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k        

nums=[1,1,2]
expectedNums=[1,2]
sol=Solution()
k=sol.removeDuplicates(nums)

k=len(expectedNums)
for i in range(0,k):
    nums[i]==expectedNums[i]