# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # count = 1
        # curr = head

        # while curr.next != None:
        #     count += 1
        #     curr = curr.next

        # mid = count // 2

        # pointer = head
        # for _ in range(mid):
        #     pointer = pointer.next

        # return pointer

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow