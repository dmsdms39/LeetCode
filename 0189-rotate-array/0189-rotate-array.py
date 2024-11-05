class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        a = k % len(nums)
        right = nums[:-a]
        left = nums[-a:]
        nums[:] = left + right
        return nums
        