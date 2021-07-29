class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
          return 1

        n1 = 1
        n2 = 2

        for _ in range(3, n+1):
          n1, n2 = n2, n1+n2

        return n2