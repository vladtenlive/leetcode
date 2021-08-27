class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        vote = 0

        for num in nums:
            if vote == 0:
                candidate = num
            if num == candidate:
                vote += 1
            else:
                vote -= 1

        return candidate

    # def majorityElement(self, nums: List[int]) -> int:
        # nums = sorted(nums)
        # return nums[len(nums)//2]