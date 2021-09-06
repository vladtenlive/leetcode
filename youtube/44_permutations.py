class Solution:
    result = []
    
    def backtrack(self, current, nums):
      if current == len(nums):
        self.result.append(nums[:])
        return
      
      for i in range(current, len(nums)):
        nums[i], nums[current] = nums[current], nums[i]
        self.backtrack(current + 1, nums)
        nums[i], nums[current] = nums[current], nums[i]
  
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack(0, nums)
        return self.result
