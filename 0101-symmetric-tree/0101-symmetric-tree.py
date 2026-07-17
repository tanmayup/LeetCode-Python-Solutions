# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return []

        q = [[root], []]
        ans = []
        level = [root.val]
        while level != []:
            ans.append(level)
            level = []
            for el in q[0]:
                if el.left:
                    q[1].append(el.left)
                    level.append(el.left.val)
                else:
                    level.append(None)
                if el.right:
                    q[1].append(el.right)
                    level.append(el.right.val)
                else:
                    level.append(None)

            q.pop(0)
            q.append([])

        for el in ans:
            copy = []
            copy[:] = el[:]
            el.reverse()
            if el != copy:
                return False
        
        return True