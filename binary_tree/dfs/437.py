# https://leetcode.com/problems/path-sum-iii/

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, target, path_values):
            if not node:
                return 0

            count = 0

            path_values.append(node.val)

            path_sum = 0
            for num in path_values[::-1]:
                path_sum += num
                if path_sum == target:
                    count += 1

            count += dfs(node.left, target, path_values)
            count += dfs(node.right, target, path_values)

            path_values.pop()

            return count

        return dfs(root, targetSum, [])
