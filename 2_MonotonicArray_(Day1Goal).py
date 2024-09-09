class Solution(object):
    def isMonotonic(self,nums):
         increasing= True
         decreasing =True
         for i in range(1,len(nums)):
                if(nums[i]<nums[i-1]):
                   increasing=False  
                if(nums[i]>nums[i-1]):
                    decreasing=False
         return increasing or decreasing     

sol=Solution()
nums=[1,2,2,3]
n=len(nums) 
result=sol.isMonotonic(nums)
print(result)