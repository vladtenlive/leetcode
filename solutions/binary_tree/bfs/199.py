# https://leetcode.com/problems/binary-tree-right-side-view/

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = deque([root])

        result = []

        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == n - 1:
                    result.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return result
