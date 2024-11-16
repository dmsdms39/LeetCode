class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            while i < len(nums) and nums[i] == val:
                nums.remove(val)
            
                

        