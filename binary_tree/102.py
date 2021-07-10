# https://leetcode.com/problems/binary-tree-level-order-traversal/

class Solution:
    import queue

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            current_level = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                current_level.append(node.val)
            result.append(current_level)

        return result
