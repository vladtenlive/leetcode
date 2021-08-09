# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode(0)
        result = merged

        while l1 and l2:
            if l1.val < l2.val:
                merged.next = ListNode(l1.val)
                l1 = l1.next
            else:
                merged.next = ListNode(l2.val)
                l2 = l2.next

            merged = merged.next

        while l1:
            merged.next = ListNode(l1.val)
            l1 = l1.next
            merged = merged.next
        while l2:
            merged.next = ListNode(l2.val)
            l2 = l2.next
            merged = merged.next

        return result.next