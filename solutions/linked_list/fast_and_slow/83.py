# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        lazy = head
        result = lazy
        pointer = head.next

        while pointer != None:
            if lazy.val != pointer.val:
                lazy.next = pointer
                lazy = lazy.next
            pointer = pointer.next

        if lazy.next != None:
            if lazy.val == lazy.next.val:
                lazy.next = None

        return result
