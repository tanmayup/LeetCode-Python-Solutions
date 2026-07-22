class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        count = 0
        idx = 1
        while idx < len(arr) - 1:
            if arr[idx] > arr[idx-1] and arr[idx] > arr[idx+1]:
                i, j = idx, idx
                while i > 0 and arr[i] > arr[i-1]:
                    i -= 1
                while j < len(arr)-1 and arr[j] > arr[j+1]:
                    j += 1
                count = max(count, j-i+1)
                idx = j+1
            else:
                idx += 1
        return count