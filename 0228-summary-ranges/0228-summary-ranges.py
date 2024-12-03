class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n < 1: return []
        gapCnt = nums[-1] - nums[0] + 1 - n
        gapIdx = []

        for i in range(1, n):
            if nums[i] - nums[i - 1] != 1:
                gapIdx.append(i) # 1, 4, 5
                # 0-0, 1-3, 4-4, 5-6
            if len(gapIdx) == gapCnt:
                break

        start = 0
        gapIdx.append(n)
        result = []

        for idx in gapIdx:
            numsRange = str(nums[start])
            if start < idx - 1:
                numsRange += "->" + str(nums[idx - 1])

            start = idx
            result.append(numsRange)

        return result
