# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = list1, list2
        if not c1:
            return c2
        if not c2:
            return c1

        if c1.val <= c2.val:
            head = c1
            c1 = c1.next
        else:
            head = c2
            c2 = c2.next

        curr = head
        while c1 or c2:
            if not c1:
                curr.next = c2
                c2 = c2.next
                curr = curr.next
                continue
            if not c2:
                curr.next = c1
                c1 = c1.next
                curr = curr.next
                continue

            if c1.val <= c2.val:
                curr.next = c1
                c1 = c1.next
            else:
                curr.next = c2
                c2 = c2.next
            curr = curr.next

        return head