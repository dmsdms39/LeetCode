class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n

        l = 2
        for r in range(2, n):
            if nums[l - 2] != nums[r]:
                nums[l] = nums[r]
                l += 1
                
        return l