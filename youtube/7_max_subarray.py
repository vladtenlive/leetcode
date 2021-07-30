class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      result_sum = nums[0]
      current_sum = nums[0]

      for i in range(1, len(nums)):
        num = nums[i]

        current_sum = max(num, current_sum + num)
        result_sum = max(current_sum ,result_sum)


      return result_sum