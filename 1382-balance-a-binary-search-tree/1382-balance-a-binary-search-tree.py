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
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ino = self.inorder(root)

        def balance(l, r) -> TreeNode:
            if l > r:
                return None

            mid = (l + r) // 2

            node = TreeNode(ino[mid])
            node.left = balance(l, mid-1)
            node.right = balance(mid+1, r)
            
            return node

        return balance(0, len(ino)-1)