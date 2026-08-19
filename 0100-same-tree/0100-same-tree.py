# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def traversal(self, root):
    #     level = [root]
    #     ans = []

    #     if not root:
    #         return []

    #     while level:
    #         nxt = []
    #         for node in level:
    #             if node:
    #                 if node.left:
    #                     nxt.append(node.left)
    #                 else:
    #                     nxt.append(None)
                
    #                 if node.right:
    #                     nxt.append(node.right)
    #                 else:
    #                     nxt.append(None)

    #         level_val = []
    #         for node in level:
    #             if node:
    #                 level_val.append(node.val)
    #             else:
    #                 level_val.append(None)

    #         ans.append(level_val)

    #         level = nxt

    #     return ans

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # return self.traversal(p) == self.traversal(q)

        st = [(p, q)]

        while st:
            node1, node2 = st.pop()

            if not node1 and not node2:
                continue
            elif None in [node1, node2] or node1.val != node2.val:
                return False

            st.append((node1.left, node2.left))
            st.append((node1.right, node2.right))

        return True