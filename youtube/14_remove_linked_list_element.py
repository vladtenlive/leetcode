# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        result = ListNode(0)
        result.next = head

        current = result

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return result.next