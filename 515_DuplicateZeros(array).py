'''Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the 
remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above 
modifications to the input array in place and do not return anything.

 '''
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        count=arr.count(0)
        n=len(arr)
        for i in range(n-1,-1,-1):
            if i+count<n:
                arr[i+count]=arr[i]

            if arr[i]==0:
                count-=1
                if i+count<n:
                    arr[i+count]=0 

arr=[1,0,2,3,0,4,5,0]
sol=Solution()
print(sol.duplicateZeros(arr))                

