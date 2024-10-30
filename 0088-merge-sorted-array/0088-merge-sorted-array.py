
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        nums1[m:] = nums2[:n]  # nums1의 뒤쪽 부분을 nums2의 처음 n개의 요소로 대체
        nums1.sort() 