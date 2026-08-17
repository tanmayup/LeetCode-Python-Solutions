# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         l, r = root.left, root.right
#         if (not r) and (not l):
#             return 1

#         elif (not r):
#             return self.minDepth(l) + 1

#         elif (not l):
#             return self.minDepth(r) + 1

#         else:
#             return min(self.minDepth(l), self.minDepth(r)) + 1

# ----------This was DFS-----------------

# ---------Now coming BFS----------------
        if not root:
            return 0

        level = [root]
        depth = 1

        while level:
            next_level = []
            for node in level:
                if not node.right and not node.left:
                    return depth

                if node.right:
                    next_level.append(node.right)

                if node.left:
                    next_level.append(node.left)

            level = next_level
            depth += 1