class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
      left = 0
      right = len(letters) - 1

      while left <= right:
        middle = left + (right - left) // 2

        if letters[middle] > target:
          right = middle - 1
        else:
          left = middle + 1

      return letters[left % len(letters)]

