# https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        start = 0
        window_sum = 0
        min_sum = float('inf')

        for end in range(len(nums)):
            window_sum += nums[end]

            while window_sum >= target:
              min_sum = min(min_sum, end - start + 1)

              window_sum -= nums[start]
              start += 1

        return 0 if min_sum == float('inf') else min_sum