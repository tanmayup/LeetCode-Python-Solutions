# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def order(self, root):
        if not root:
            return []
        else:
            return self.order(root.left) + [root.val] + self.order(root.right)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        seq = self.order(root)
        if key in seq:
            seq.remove(key)
        else:
            return root
        
        if len(seq) != 0:
            root = TreeNode(seq[0])
        else:
            return None
        curr = root
        for el in seq[1:]:
            curr.right = TreeNode(el)
            curr = curr.right


        return root
        