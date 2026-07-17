class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # dict1 = {}
        # for i in range(len(numbers)):
        #     rem = target - numbers[i]
        #     if rem in dict1:
        #         return [dict1[rem]+1, i+1]

        #     dict1[numbers[i]] = i

        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

            elif numbers[left] + numbers[right] > target:
                right -= 1

            else:
                left += 1