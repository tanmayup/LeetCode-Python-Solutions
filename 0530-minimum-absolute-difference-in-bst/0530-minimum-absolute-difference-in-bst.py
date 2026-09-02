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
        return self.inorder(root.left) + [root] + self.inorder(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ino = self.inorder(root)
        diff = float("inf")
        for i in range(len(ino)-1):
            diff = min(diff, ino[i+1].val-ino[i].val)

        return diff