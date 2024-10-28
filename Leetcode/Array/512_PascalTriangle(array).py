'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []

        l=[[1]]
        for i in range(1,numRows):
            row=[1]
            for j in range(1,i):
                row.append(l[i-1][j-1]+l[i-1][j])

            row.append(1)
            l.append(row)
        return l    

numRows=5
sol=Solution()
print(sol.generate(numRows))       