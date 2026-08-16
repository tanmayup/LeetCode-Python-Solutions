# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # level = [root]
        # ans = [root.val]

        # while level:
        #     lc = []
        #     lc[:] = level[:]
        #     for el in lc:
        #         if el.right:
        #             level.append(el.right)
        #         if el.left:
        #             level.append(el.left)
        #         level.remove(el)

        #     if not level:
        #         break
        #     sm = 0
        #     for el in level:
        #         sm += el.val
        #     ans.append(sm/len(level))

        # return ans

        level = [root]
        ans = []

        while level:
            total = 0
            next_level = []

            for node in level:
                total += node.val

                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
            ans.append(total/len(level))
            level = next_level

        return ans