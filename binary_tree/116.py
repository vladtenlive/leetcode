# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        origin = root
        q = deque([root])

        while q:
            n = len(q)
            prev = None
            for i in range(n):
                node = q.popleft()
                if i == n - 1:
                    node.next = None
                if prev:
                    prev.next = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                prev = node

        return origin
