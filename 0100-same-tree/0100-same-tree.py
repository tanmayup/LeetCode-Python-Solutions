# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root):
        level = [root]
        ans = []

        if not root:
            return []

        while level:
            nxt = []
            for node in level:
                if node:
                    if node.left:
                        nxt.append(node.left)
                    else:
                        nxt.append(None)
                
                    if node.right:
                        nxt.append(node.right)
                    else:
                        nxt.append(None)

            level_val = []
            for node in level:
                if node:
                    level_val.append(node.val)
                else:
                    level_val.append(None)

            ans.append(level_val)

            level = nxt

        return ans

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traversal(p) == self.traversal(q)