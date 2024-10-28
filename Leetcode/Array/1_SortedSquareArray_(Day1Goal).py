# Question 1: Sorted Squared Array - You are given an array of Integers in which each subsequent value
# is not less than the previous value. Write a function that takes this array as an input and 
# returns a new array with the squares of each number sorted in ascending order.

# function
def sortedsquare(arr,n):
    for i in range(n):
        arr[i]=arr[i]*arr[i]
    arr.sort()    


arr=[-4,-1,0,3,10]
n=len(arr)

print("Before sort")
for i in range(n):
    print(arr[i],end= ' ')
print("\n")   

print("After sort")
sortedsquare(arr,n)
for i in range(n):
    print(arr[i],end= ' ')
print("\n")

# or

# class Solution(object):
#     def sortedSquares(self, nums):
#         for i in range(len(nums)):
#             nums[i] = nums[i] * nums[i]

#         nums.sort()            
#         return nums

# sol = Solution()
# arr = [-4, -1, 0, 3, 10]
# result = sol.sortedSquares(arr) 
# print(result)