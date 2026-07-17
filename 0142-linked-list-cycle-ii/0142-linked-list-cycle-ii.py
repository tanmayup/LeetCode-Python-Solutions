# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        cycle = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                cycle = True
                break

        if cycle == False:
            return None

        cl = 1
        slow = slow.next
        while slow != fast:
            cl += 1
            slow = slow.next

        p1, p2 = head, head
        # for _ in range(cl-1):
        #     p2 = p2.next

        for _ in range(cl):
            p2 = p2.next

        # while True:
        #     prev = p1
        #     p1 = p1.next
        #     p2 = p2.next
        #     if p2 == prev:
        #         return prev

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1