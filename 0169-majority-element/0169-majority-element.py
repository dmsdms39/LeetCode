class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}  # 일반 딕셔너리 사용

        # 각 숫자의 개수를 세기
        for i in nums:
            hash[i] = hash.get(i, 0) + 1

        # 최대값을 가지는 키를 찾기
        max_key = max(hash, key=hash.get)
        return max_key