class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        print(len(nums), k)
        ihash = {}
        for i in range(len(nums)):
            if nums[i] in ihash and abs(i - ihash[nums[i]]) <= k:
                return True
            # store "nums index" in ihash hashmap by "nums key"
            ihash[nums[i]] = i
        return False
