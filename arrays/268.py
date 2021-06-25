# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ideal_sum = n*(n+1)/2
        return int(ideal_sum - sum(nums))
