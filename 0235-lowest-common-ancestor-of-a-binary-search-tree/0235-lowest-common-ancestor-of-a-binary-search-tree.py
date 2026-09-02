# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root:
        #     return None

        # if root == p or root == q:
        #     return root

        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left and right:
        #     return root

        # elif left:
        #     return left

        # elif right:
        #     return right

        # else:
        #     return None

# ===================================

        # if not root:
        #     return None

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root

# =================================

        small, large = min(p.val, q.val), max(p.val, q.val)

        while root:
            if root.val > large:
                root = root.right

            elif root.val < small:
                root = root.left

            else:
                return root