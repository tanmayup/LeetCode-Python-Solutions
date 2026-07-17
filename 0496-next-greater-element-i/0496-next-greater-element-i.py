class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans = []
        # for num in nums1:
        #     idx = nums2.index(num)
        #     nge = -1
        #     for el in nums2[idx:]:
        #         if el > num:
        #             nge = el
        #             break
        #     ans.append(nge)

        # return ans
        
        stack = []
        ans = [0] * len(nums2)
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if not stack:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
            stack.append(nums2[i])

        d = dict(zip(nums2, ans))
        result = []
        for i in nums1:
            # result.append(ans[nums2.index(i)])
            result.append(d[i])

        return result