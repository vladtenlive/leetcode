class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_column = False
        rows = len(matrix)
        columns = len(matrix[0])
        
        for i in range(rows):
          
          if matrix[i][0] == 0:
            first_column = True
          
          for j in range(1, columns):
            if matrix[i][j] == 0:
              matrix[i][0] = 0
              matrix[0][j] = 0
              
              
        for i in range(1, rows):
          for j in range(1, columns):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
              matrix[i][j] = 0
           
        if matrix[0][0] == 0:
          for j in range(columns):
            matrix[0][j] = 0
              
        if first_column:
          for i in range(rows):
            matrix[i][0] = 0
