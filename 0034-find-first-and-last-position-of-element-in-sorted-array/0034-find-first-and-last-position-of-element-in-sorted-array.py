class Solution:
    def lb(self, nums, target):
        l = 0
        r = len(nums) - 1
        ans = len(nums)

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                ans = mid
                r = mid - 1
            
            else:
                l = mid + 1

        return ans

    def ub(self, nums, target):
        l = 0
        r = len(nums) - 1
        ans = len(nums)

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                ans = mid
                r = mid - 1
            
            else:
                l = mid + 1

        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lb(nums, target)
        ub = self.ub(nums, target)

        if lb == ub:
            return [-1, -1]

        else:
            return [lb, ub-1]