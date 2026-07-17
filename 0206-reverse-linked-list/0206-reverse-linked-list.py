# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # l = 0
        # curr = head
        # while curr:
        #     curr = curr.next
        #     l += 1

        # while l != 0:
        #     curr = head
        #     for _ in range(l-1):
        #         curr.val, curr.next.val = curr.next.val, curr.val
        #         curr = curr.next
        #     l -= 1

        # return head

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt
        
        return prev