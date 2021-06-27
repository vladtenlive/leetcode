# https://leetcode.com/problems/permutation-in-string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        check_hash = Counter(s1)
        current_hash = defaultdict(int)

        start = 0

        for end in range(len(s2)):
            char = s2[end]
            current_hash[char] += 1

            if end - start + 1 == len(s1):
                if current_hash == check_hash:
                    return True

                char = s2[start]
                current_hash[char] -= 1
                if current_hash[char] == 0:
                    del current_hash[char]

                start += 1

        return False
