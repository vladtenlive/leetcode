class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0 for _ in range(n)]

        left = 0
        right = n - 1

        for i in range(n-1, -1, -1):
          if nums[left] ** 2 > nums[right] ** 2:
            result[i] = nums[left] ** 2
            left += 1
          else:
            result[i] = nums[right] ** 2
            right -= 1

        return result