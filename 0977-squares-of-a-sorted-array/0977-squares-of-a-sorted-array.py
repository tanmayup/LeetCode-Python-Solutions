class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # # if nums[0] >= 0:
        # #     return [num**2 for num in nums]

        # # if nums[-1] < 0:
        # #     return [num**2 for num in nums[::-1]]

        # pos = len(nums)
        # for i in range(len(nums)):
        #     if nums[i] >= 0:
        #         pos = i
        #         break

        # a, b = 0, 0
        # ans = []
        # nl = nums[:pos][::-1]
        # pl = nums[pos:]
        # while a < len(nl) and b < len(pl):
        #     n, p = nl[a], pl[b]
        #     if p**2 <= n**2:
        #         ans.append(p**2)
        #         b += 1
        #     else:
        #         ans.append(n**2)
        #         a += 1

        # if a == len(nl):
        #     ans += [num**2 for num in pl[b:]]
        # else:
        #     ans += [num**2 for num in nl[a:]]

        # return ans

        n = len(nums)
        r = n-1
        l = 0

        ans = [-1] * n
        pointer = -1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans[pointer] = nums[l] ** 2
                l += 1
            else:
                ans[pointer] = nums[r] ** 2
                r -= 1
            pointer -= 1

        return ans