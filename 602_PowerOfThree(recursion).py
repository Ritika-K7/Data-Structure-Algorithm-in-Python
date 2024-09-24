'''Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for x in range(0,pow(3,5)-1):
            if n==3**x:
                return True

n=27
sol=Solution()
print(sol.isPowerOfThree(n))         