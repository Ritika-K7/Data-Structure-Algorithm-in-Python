class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]  # Swap the elements
            left += 1
            right -= 1

s = ["h", "e", "l", "l", "o"]
R = Solution()
R.reverseString(s)
print(s)


# OR 
# class Solution(object):
#     def reverseString(self, s):
#         return s[::-1]  
# s = ["h", "e", "l", "l", "o"]
# R = Solution()
# reversed_s = R.reverseString(s)  
# print(reversed_s)  
