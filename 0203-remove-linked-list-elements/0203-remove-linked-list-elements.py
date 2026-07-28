# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # if not head:
        #     return head
        
        # curr, prev = head, head
        # while curr:
        #     if curr.val != val:
        #         prev = curr
        #         curr = curr.next

        #     else:
        #         if curr == head:
        #             prev = curr
        #             curr = curr.next
        #             head = curr
        #             prev.next = None
        #         else:
        #             curr = curr.next
        #             prev.next = curr

        # return head

        if not head:
            return head

        dummyh = ListNode(-1)
        dummyh.next = head

        curr = dummyh

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummyh.next