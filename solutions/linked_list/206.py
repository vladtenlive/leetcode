# https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev = None
        current = head

        while current != None:
            move_to = current.next
            current.next = prev
            prev = current
            current = move_to

        return prev
