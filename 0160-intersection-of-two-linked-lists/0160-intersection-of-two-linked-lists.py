# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # l1, l2 = 0, 0
        # curr1 = headA
        # curr2 = headB
        # while curr1:
        #     curr1 = curr1.next
        #     l1 += 1

        # while curr2:
        #     curr2 = curr2.next
        #     l2 += 1

        # if l1 >= l2:
        #     startA = headA
        #     for _ in range(l1 - l2):
        #         startA = startA.next
        #     startB = headB
        # else:
        #     startB = headB
        #     for _ in range(l2 - l1):
        #         startB = startB.next
        #     startA = headA

        # while startA:
        #     if startA == startB:
        #         return startA
        #     startA = startA.next
        #     startB = startB.next

        # return None

        # p1, p2 = headA, headB
        # while True:
        #     if p1 == p2:
        #         return p1

        #     if p1.next == None and p2.next == None:
        #         return None
        #     elif p1.next == None:
        #         p1 = headB
        #         p2 = p2.next
        #     elif p2.next == None:
        #         p2 = headA
        #         p1 = p1.next
        #     else:
        #         p1 = p1.next
        #         p2 = p2.next

        p1, p2 = headA, headB
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            
            if p2:
                p2 = p2.next
            else:
                p2 = headA

        return p1