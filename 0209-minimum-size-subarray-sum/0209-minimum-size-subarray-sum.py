class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target :
            return 0

        minCnt = 1e9
        l = r = 0
        sumRslt = nums[0]

        while r < len(nums):
            if sumRslt < target:
                r += 1
                if r <= len(nums) - 1:
                    sumRslt += nums[r]
            else:
                minCnt = min(minCnt, r - l + 1)
                sumRslt -= nums[l]
                l += 1
        if minCnt == 1e9:
            return 0

        return minCnt