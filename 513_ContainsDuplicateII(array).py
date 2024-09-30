'''Given an integer array nums and an integer k, return true if there are two distinct 
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j] and abs(i-j)<=k:
        #             return True
        # return False   
        num_dict={}
        for i in range(len(nums)):
            if nums[i] in num_dict and abs(i-num_dict[nums[i]])<=k:
                return True
            num_dict[nums[i]]=i
        return False    

nums=[1,2,3,1]
k=3 
sol=Solution()
print(sol.containsNearbyDuplicate(nums,k))      