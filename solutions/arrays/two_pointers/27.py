# https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        remove_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[remove_index] = nums[i]
                remove_index += 1

        return remove_index
