'''Write a function that takes the binary representation of a positive integer and returns the number of 
set bits
 it has (also known as the Hamming weight).'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return '0'

        binary=''    
        while n>0:
            r=n%2
            binary=str(r)+binary   
            n=n//2
        
        count=0
        for i in str(binary):
            if(i=='1'):
                count+=1
        return count

n=11
sol=Solution()
print(sol.hammingWeight(n))
