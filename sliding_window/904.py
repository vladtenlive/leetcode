# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        result = float('-inf')
        basket = defaultdict(int)
        start = 0

        for end in range(len(tree)):
            fruit = tree[end]
            basket[fruit] += 1

            while len(basket) > 2:
                fruit = tree[start]

                basket[fruit] -= 1
                if basket[fruit] == 0:
                    del basket[fruit]

                start += 1

            result = max(result, end - start + 1)

        return result if result != float('-inf') else 0
