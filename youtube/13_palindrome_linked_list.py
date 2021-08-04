# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
          return True

        middle = self.middleNode(head)
        reverse = self.reverseList(middle)

        while reverse:
          if head.val != reverse.val:
            return False

          reverse = reverse.next
          head = head.next

        return True

    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        return prev