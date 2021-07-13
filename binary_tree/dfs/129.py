# https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, tree_sum):
            if not node:
                return 0

            tree_sum = tree_sum * 10 + node.val
            if not node.left and not node.right:
                return tree_sum

            return dfs(node.left, tree_sum) + dfs(node.right, tree_sum)

        return dfs(root, 0)
