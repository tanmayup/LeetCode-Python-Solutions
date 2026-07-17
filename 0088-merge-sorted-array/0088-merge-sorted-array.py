class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1c = nums1[:m]

        i, j, count = 0, 0, 0
        while i != m and j != n:
            if nums1c[i] < nums2[j]:
                nums1[count] = nums1c[i]
                i += 1
            else:
                nums1[count] = nums2[j]
                j += 1
            count += 1

        if i == m:
            nums1[(count):] = nums2[j:]
        else:
            nums1[(count):] = nums1c[i:]

        # if n == 1:
        #     l = nums1c + nums2
        #     nums1[:] = l[:]

        # if n == 0:
        #     nums1[:] = nums1c[:]

        # elif m == 0:
        #     nums1[:] = nums2[:]