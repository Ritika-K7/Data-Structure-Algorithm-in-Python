'''Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for x in range(0,pow(2,10)-1):
            if n==2**x:
                return True

        
n=1
sol=Solution()
print(sol.isPowerOfTwo(n))        