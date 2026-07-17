# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                if el.right:
                    q[1].append(el.right)
                    level.append(el.right.val)

            q.pop(0)
            q.append([])

        return ans