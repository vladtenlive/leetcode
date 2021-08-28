class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         left = [1 for _ in range(n)]
#         right = [1 for _ in range(n)]

#         for i in range(1, n) :
#           left[i] = left[i - 1] * nums[i - 1]

#         for i in range(n-2, -1, -1):
#           right[i] = right[i + 1] * nums[i + 1]

#         result = []
#         for i in range(n):
#           result.append(left[i] * right[i])

#         return result

        n = len(nums)
        result = [1 for _ in range(n)]

        for i in range(1, n) :
          result[i] = result[i - 1] * nums[i - 1]

        right = 1
        for i in range(n-1, -1, -1):
          result[i] *= right
          right *= nums[i]

        return result

