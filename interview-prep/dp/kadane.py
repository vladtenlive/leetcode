    def kadane(self, nums):
        max_sum = nums[0]
        current_sum = nums[0]
        
        max_start = 0
        max_end = 0
        
        start = 0
        
        for i in range(1, len(nums)):
          current_sum += nums[i]
          if current_sum < nums[i]:
            current_sum = nums[i]
            start = i
          if max_sum < current_sum:
            max_end = i
            max_start = start
            max_sum = current_sum
            
        return max_start, max_end, max_sum
