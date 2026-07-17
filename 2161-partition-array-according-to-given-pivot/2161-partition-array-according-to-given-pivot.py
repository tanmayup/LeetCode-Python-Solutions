class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        plist, small, big = [], [], []
        for num in nums:
            if num == pivot:
                plist.append(num)
            
            elif num > pivot:
                big.append(num)
            
            else:
                small.append(num)

        return small + plist + big