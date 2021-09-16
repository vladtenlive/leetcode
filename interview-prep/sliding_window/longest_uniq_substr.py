class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        left = 0
        result = 0
        
        for right in range(len(s)):
          counter[s[right]] += 1
          
          while len(counter) != right - left + 1:
            left_char = s[left]
            counter[left_char] -= 1
            if counter[left_char] == 0:
              del counter[left_char]
            
            left += 1
          
          result = max(result, right - left + 1)
        
        
        return result
