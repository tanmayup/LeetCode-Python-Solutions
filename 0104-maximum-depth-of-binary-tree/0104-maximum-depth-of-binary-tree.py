# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0

        # q = [[root], []]
        # ans = []
        # level = [root.val]
        # while level != []:
        #     ans.append(level)
        #     level = []
        #     for el in q[0]:
        #         if el.left:
        #             q[1].append(el.left)
        #             level.append(el.left.val)
        #         if el.right:
        #             q[1].append(el.right)
        #             level.append(el.right.val)

        #     q.pop(0)
        #     q.append([])

        # return len(ans)
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1