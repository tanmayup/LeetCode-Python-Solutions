# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        ans = ListNode()
        curr = ans
        carry = 0

        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0

            add = v1 + v2 + carry
            carry = add // 10
            curr.val = add % 10
            curr.next = ListNode()
            curr = curr.next

            if p1 == None:
                p2 = p2.next
            elif p2 ==  None:
                p1 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next
            
        if carry == 1:
            curr.val = carry
        else:
            curr = ans
            while curr.next.next:
                curr = curr.next
            curr.next = None

        return ans