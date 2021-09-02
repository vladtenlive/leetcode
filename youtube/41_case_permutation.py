class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.result = []
        self.traverse("", s, 0)
        return self.result
      
    def traverse(self, current, s, i):
      if len(current) == len(s):
        self.result.append(current)
        return
      
      self.traverse(current + s[i], s, i + 1)
      if s[i].isalpha():
        self.traverse(current + s[i].swapcase(), s, i + 1)
