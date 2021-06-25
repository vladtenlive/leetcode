# https://leetcode.com/problems/remove-linked-list-elements/

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        result = ListNode()

        pointer = result
        pointer.next = head

        while pointer != None and pointer.next != None:

            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next

        return result.next
