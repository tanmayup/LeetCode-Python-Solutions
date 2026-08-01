# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        fh, sh = head, prev

        while sh:
            if sh.val != fh.val:
                return False
            fh = fh.next
            sh = sh.next

        return True