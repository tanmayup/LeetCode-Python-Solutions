class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        count = 0
        for idx, val in enumerate(arr):
            if idx > 0 and idx < len(arr)-1 and val > arr[idx-1] and val > arr[idx+1]:
                i, j = idx, idx
                while i > 0 and arr[i] > arr[i-1]:
                    i -= 1
                while j < len(arr)-1 and arr[j] > arr[j+1]:
                    j += 1
                count = max(count, j-i+1)

        return count