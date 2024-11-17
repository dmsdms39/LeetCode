class Solution:
    def canJump(self, nums: List[int]) -> bool:
        distance = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= distance:
                distance = i

        return True if distance == 0 else False