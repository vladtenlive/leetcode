class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        direction = 0

        while top <= bottom and left <= right:
          if direction == 0:
            for i in range(left, right + 1):
              result.append(matrix[top][i])

            top += 1
            direction = 1

          elif direction == 1:
            for i in range(top, bottom + 1):
              result.append(matrix[i][right])

            right -= 1
            direction = 2

          elif direction == 2:
            for i in range(right, left - 1, -1):
              result.append(matrix[bottom][i])

            bottom -= 1
            direction = 3

          elif direction == 3:
            for i in range(bottom, top - 1, -1):
              result.append(matrix[i][left])

            left += 1
            direction = 0

        return result