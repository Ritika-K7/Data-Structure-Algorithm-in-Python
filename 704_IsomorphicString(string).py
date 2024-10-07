'''Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 '''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.trans(s)==self.trans(t)
         
    def trans(self,p):
        dict={}
        l=[]
        for i in range(len(p)):
            if p[i] not in dict:
                dict[p[i]]=i
            l.append(str(dict[p[i]]))    
        return " ".join(l)  

          

s='egg'
t='add'
sol=Solution()
print(sol.isIsomorphic(s,t))        