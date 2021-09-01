class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        rows = len(matrix)
        columns = len(matrix[0])
        
        up = 0
        left = 0
        right = columns - 1
        down = rows - 1
        
        direction = 0
        
        while up <= down and left <= right:
          
          if direction == 0:
            for i in range(left, right + 1):
              result.append(matrix[up][i])

            up += 1
            direction = 1
            
          elif direction == 1:
              for i in range(up, down + 1):
                result.append(matrix[i][right])

              right -= 1
              direction = 2

          elif direction == 2:
              for i in range(right, left - 1, -1):
                  result.append(matrix[down][i])

              down -= 1
              direction = 3

          elif direction == 3:
              for i in range(down, up - 1, -1):
                  result.append(matrix[i][left])
                  
              left += 1
              direction = 0
        
        return result
