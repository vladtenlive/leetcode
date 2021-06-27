# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        letters = defaultdict(int)

        start = 0
        max_letter_count = 0

        for end in range(len(s)):
            letter = s[end]
            letters[letter] += 1
            max_letter_count = max(max_letter_count, letters[letter])

            if end - start + 1 - max_letter_count > k:
                letter = s[start]
                letters[letter] -= 1
                start += 1

            result = max(result, end - start + 1)

        return result
