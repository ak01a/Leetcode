class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        Manual Row Reversal:
        For each row i, iterate over the first half of the row (j ranging from 0 to n // 2 - 1).
        Swap the j-th element (matrix[i][j]) with the corresponding element from the end (matrix[i][n-1-j]).
        
        # Step 2: Reverse each row manually
        for i in range(n):
            for j in range(n // 2):
                # Swap the j-th element with the (n-1-j)-th element in the row
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

        '''
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()