# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        result = 0
        seen = {}

        for end in range(len(s)):
            end_letter = s[end]
            if end_letter in seen:
                start = max(start, seen[end_letter] + 1)
            seen[end_letter] = end
            result = max(result, end - start + 1)

        return result
