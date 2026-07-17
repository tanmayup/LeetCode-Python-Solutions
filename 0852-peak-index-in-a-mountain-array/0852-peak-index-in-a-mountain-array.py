class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 1, len(arr) - 2 

        while l <= r:
            mid = (l + r) // 2
            
            if arr[mid-1] < arr[mid] and arr[mid+1] < arr[mid]:
                return mid
                
            elif arr[mid-1] < arr[mid] and arr[mid+1] > arr[mid]:
                l = mid + 1
                
            else:
                r = mid - 1