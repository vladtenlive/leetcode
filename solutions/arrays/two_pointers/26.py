# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index-1]:
                nums[unique_index] = nums[i]
                unique_index += 1

        return unique_index
