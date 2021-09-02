class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
          for j in range(len(board[0])):
            if board[i][j] == word[0] and self.traverse(board, i, j, word):
              return True
            
        return False
      
    def traverse(self, board, i, j, word):
      if len(word) == 0:
        return True
      
      if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
        return False
        
      match = False
      original_value = board[i][j]
      board[i][j] = "_"
      
      match = self.traverse(board, i + 1, j, word[1:]) or self.traverse(board, i - 1, j, word[1:]) or self.traverse(board, i, j - 1, word[1:]) or self.traverse(board, i, j + 1, word[1:]) 
      
      board[i][j] = original_value
      
      return match
