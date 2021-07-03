# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        min_diff = float('inf')
        result = 0
        n = len(nums)

        for i in range(n):
            mid = nums[i]
            right = n - 1
            left = i + 1
            while left < right:
                current_sum = nums[left] + mid + nums[right]
                if current_sum == target:
                    return current_sum
                if abs(target - current_sum) < min_diff:
                    min_diff = abs(target - current_sum)
                    result = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result
