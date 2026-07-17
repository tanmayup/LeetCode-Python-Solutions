# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        dummy = ListNode(head.val-1, head)
        p1 = dummy
        p2 = dummy.next
        while p2 and p2.next:
            if p2.next.val != p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                while (p2.next != None) and (p2.next.val == p2.val):
                    p2 = p2.next
                p1.next = p2.next
                p2 = p2.next

        return dummy.next