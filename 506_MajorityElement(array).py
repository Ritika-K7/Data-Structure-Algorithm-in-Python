'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the
 majority element always exists in the array.'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        n=len(nums)
        for num in nums:
            if num in count:
                count[num]=count[num]+1
            else:
                count[num]=1

            if count[num]>n//2:
                return num    

nums=[3,2,3]

sol=Solution()
print(sol.majorityElement(nums))
