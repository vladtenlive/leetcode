class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for num in nums:
          result += [subset + [num] for subset in result]
        
        return result
