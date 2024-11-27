class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        partnerIdx = {}
        for i in range(len(numbers)):
            num = numbers[i]
            if num in partnerIdx:
                return [partnerIdx[num] + 1, i + 1]
            else:
                partnerIdx[target - num] = i