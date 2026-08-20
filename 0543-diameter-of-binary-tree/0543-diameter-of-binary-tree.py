# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(root):
            if not root:
                return 0

            ldepth = depth(root.left)
            rdepth = depth(root.right)

            self.diameter = max(self.diameter, ldepth + rdepth)

            return max(ldepth, rdepth) + 1

        depth(root)

        return self.diameter