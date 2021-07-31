# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        n = len(nums)

        for i in range(n):
            target = -nums[i]
            right = n - 1
            left = i + 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.add((nums[i], nums[left], nums[right]))
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return result
