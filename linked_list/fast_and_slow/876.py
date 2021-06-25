# https://leetcode.com/problems/middle-of-the-linked-list/

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        return slow
