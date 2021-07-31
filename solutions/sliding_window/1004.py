# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        result = 0

        current_zeroes = 0

        for end in range(len(nums)):
            num = nums[end]
            if num == 0:
                current_zeroes += 1

            if current_zeroes > k:
                num = nums[start]
                if num == 0:
                    current_zeroes -= 1
                start += 1

            result = max(result, end - start + 1)

        return result
