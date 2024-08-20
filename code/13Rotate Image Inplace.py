class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # mirror reflection about y axis
        for i in range(n):
            matrix[i] = matrix[i][::-1]

        # transpose
        for i in range(1,n+1):
            for j in range(i,n+1):
                matrix[i-1][-j],matrix[j-1][-i] = matrix[j-1][-i],matrix[i-1][-j]
