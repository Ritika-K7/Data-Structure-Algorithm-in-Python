# Given a sorted array of distinct integers and a target value, return the index if the target 
# is found. If not, return the index where it would be if it were inserted in order.

class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if(target==nums[i]):
                return i
            if(nums[i]>target):
                    return i
        return (len(nums))        

        
nums = [1,3,5,6]
sol=Solution()
print(sol.searchInsert(nums,5))
