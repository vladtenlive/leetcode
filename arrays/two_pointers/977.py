# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        start = 0
        end = len(nums) - 1
        result_index = len(nums) - 1

        while start <= end:
            start_num = nums[start] ** 2
            end_num = nums[end] ** 2

            if start_num > end_num:
                result[result_index] = start_num
                start += 1
            else:
                result[result_index] = end_num
                end -= 1

            result_index -= 1

        return result
