# https://leetcode.com/problems/path-sum-ii/
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        result = []

        def dfs(node, target, current_path):
            if not node:
                return

            current_path.append(node.val)

            if node.val == target and not node.right and not node.left:
                result.append(current_path[:])
                current_path.pop()
                return

            dfs(node.left, target - node.val, current_path)
            dfs(node.right, target - node.val, current_path)
            current_path.pop()

        dfs(root, targetSum, [])
        return result
