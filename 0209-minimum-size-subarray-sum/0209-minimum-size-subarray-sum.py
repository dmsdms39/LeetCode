class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target :
            return 0

        minCnt = 1e9
        l, r = 0, 0
        sumRslt = 0

        for r, val in enumerate(nums):
            sumRslt += val
            while sumRslt >= target:
                minCnt = min(minCnt, r - l + 1)
                sumRslt -= nums[l]
                l += 1
    
        return minCnt