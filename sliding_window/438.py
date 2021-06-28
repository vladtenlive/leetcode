# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern = Counter(p)
        pattern_length = len(p)

        window = defaultdict(int)

        result = []

        start = 0
        for end in range(len(s)):
            letter = s[end]
            window[letter] += 1

            if end - start + 1 == pattern_length:
                if window == pattern:
                    result.append(start)

                letter = s[start]
                window[letter] -= 1

                if window[letter] == 0:
                    del window[letter]

                start += 1

        return result
