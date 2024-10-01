'''Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # if numRows==0:
        #     return []

        l=[[1]]
        for i in range(1,rowIndex+1):
            row=[1]
            for j in range(1,i):
                row.append(l[i-1][j-1]+l[i-1][j])

            row.append(1)
            l.append(row)
        # return l  

        return l[rowIndex]


rowIndex=3
sol=Solution()
print(sol.getRow(rowIndex))