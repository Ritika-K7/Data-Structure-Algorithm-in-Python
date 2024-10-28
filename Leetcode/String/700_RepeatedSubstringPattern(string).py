'''Given a string s, check if it can be constructed by taking a substring of it and 
appending multiple copies of the substring together.'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string=s+s
        substring=string[1:-1]
        return s in substring  

s='abab'
sol=Solution()
print(sol.repeatedSubstringPattern(s))