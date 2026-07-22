class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     j = i+1
        #     while j < len(nums) and j < i+k+1:
        #         if nums[i] == nums[j]:
        #             return True
        #         j += 1
        # return False

        map = {}
        for idx, val in enumerate(nums):
            if val not in map:
                map[val] = idx
            else:
                if idx-map[val] <= k:
                    return True
                else:
                    map[val] = idx

        return False    