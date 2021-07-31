# https://leetcode.com/problems/diameter-of-binary-tree/
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.result = 1

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.result = max(self.result, left+right+1)
            return max(left, right) + 1

        dfs(root)
        return self.result - 1  # same root node count twices
