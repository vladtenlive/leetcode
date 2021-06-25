# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        missing_num = 0
        for num in nums:
            missing_num ^= num
        return missing_num
