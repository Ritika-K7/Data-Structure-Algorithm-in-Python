"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 """

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count =0
        for i in range(0,len(nums)):
            if nums[i]==0:
                count+=1 
        nums[:]=[x for x in nums if x != 0]
      
        nums.extend([0]*count)

        return nums

nums=[0,1,0,3,12] 
sol=Solution()
print(sol.moveZeroes(nums))        