'''Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # for i in range(0,len(s)):
        #     for j in range(0,len(t)):
        #          if len(s) and s[i] == len(t) and t[j]:
        #              return True
        return sorted(s)==sorted(t)


s='anagram'
t='nagaram'
sol=Solution()
print(sol.isAnagram(s,t))            
        