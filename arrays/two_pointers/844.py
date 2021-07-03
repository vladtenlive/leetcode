# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def get_string_index(self, s: str, index: int) -> int:
        to_skip = 0
        while index >= 0:
            if s[index] == "#":
                to_skip += 1
            elif to_skip > 0:
                to_skip -= 1
            else:
                break
            index -= 1

        return index

    def backspaceCompare(self, s: str, t: str) -> bool:
        s_index = len(s) - 1
        t_index = len(t) - 1

        while s_index >= 0 or t_index >= 0:
            s_index = self.get_string_index(s, s_index)
            t_index = self.get_string_index(t, t_index)

            if s_index < 0 and t_index < 0:
                return True
            if s_index < 0 or t_index < 0:
                return False
            if s[s_index] != t[t_index]:
                return False

            t_index -= 1
            s_index -= 1

        return True
