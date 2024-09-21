'''Given a non-empty array of integers nums, every element appears twice except for one.
 Find that single one.'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for num in nums:
            result^=num  
        return result      

nums=[2,2,1]
sol=Solution()
print(sol.singleNumber(nums))       