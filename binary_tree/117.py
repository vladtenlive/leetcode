# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


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
