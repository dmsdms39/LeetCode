class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        partnerIdx = {}
        for i in range(len(numbers)):
            if numbers[i] in partnerIdx:
                return [partnerIdx[numbers[i]] + 1, i + 1]
            else:
                partnerIdx[target - numbers[i]] = i