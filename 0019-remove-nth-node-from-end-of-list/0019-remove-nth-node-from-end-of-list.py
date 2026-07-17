# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # l = 0
        # curr = head
        # while curr:
        #     l += 1
        #     curr = curr.next

        # idx = l - n

        # if idx == 0:
        #     return head.next

        # el = head
        # for _ in range(idx-1):
        #     el = el.next
        # el.next = el.next.next
        # return head


        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        if fast == None:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head