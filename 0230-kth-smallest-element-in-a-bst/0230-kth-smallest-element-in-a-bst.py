# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # for _ in range(k):
        #     sm = root
        #     prev = root
        #     if not sm:
        #         ans = -1
        #     if not sm.left:
        #         if root.right:
        #             root = root.right
        #         ans = sm.val

        #     while sm.left:
        #         prev = sm
        #         sm = sm.left
        #     ans = sm.val
        #     prev.left = sm.right if sm.right else None

        # return ans

        return self.inorder(root)[k-1]