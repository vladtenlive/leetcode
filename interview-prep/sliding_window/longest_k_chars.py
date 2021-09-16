class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        counter = defaultdict(int)
        result = 0
        
        for right in range(len(s)):
          counter[s[right]] += 1
          
          while len(counter) > k:
            counter[s[left]] -= 1
            if counter[s[left]] == 0:
              del counter[s[left]]
            left += 1
            
          result = max(result, right - left + 1)
            
        return result      
