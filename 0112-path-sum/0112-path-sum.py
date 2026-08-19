# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def dfs(self, node, rem):
    #     if not node:
    #         return False

    #     rem -= node.val

    #     if not node.right and not node.left:
    #         return rem == 0

    #     return self.dfs(node.left, rem) or self.dfs(node.right, rem)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # return self.dfs(root, targetSum)

        if not root:
            return False

        st = [(root, root.val)]

        while st:
            curr, val = st.pop()

            if not curr.left and not curr.right and val == targetSum:
                return True

            if curr.left:
                st.append((curr.left, curr.left.val + val))

            if curr.right:
                st.append((curr.right, curr.right.val + val))

        return False