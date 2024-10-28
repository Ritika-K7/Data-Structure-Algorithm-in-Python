'''Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.'''

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for x in range(0,pow(2,10)-1):
            if n==4**x:
                return True
n=16
sol=Solution()
print(sol.isPowerOfFour(n))