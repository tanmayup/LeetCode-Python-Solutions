# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1
        
        if (l == 0) or (l == 1):
            return head
        for _ in range(k%l):
            last = head.next
            slast = head
            while last.next:
                last = last.next
                slast = slast.next

            last.next = head
            slast.next = None
            head = last

        return head

        # if head == None or head.next == None:
        #     return head

        # l = 1
        # last = head
        # while last.next:
        #     last = last.next
        #     l += 1

        # k = k % l
        # if k == 0:
        #     return head

        # curr = head
        # for _ in range(l-k-1):
        #     curr = curr.next
        # last.next = head
        # head = curr.next
        # curr.next = None

        # return head        