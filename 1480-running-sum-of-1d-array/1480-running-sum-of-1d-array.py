class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # runsum = []
        # for i in range(len(nums)):
        #     runsum.append(sum(nums[j] for j in range(i+1)))

        # return runsum

        runsum = []
        sum = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            runsum.append(sum)

        return runsum