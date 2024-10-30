class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            # 현재 결과 리스트를 반대로 읽고, 각 숫자에 2^i를 더해줌
            result += [x + (1 << i) for x in reversed(result)]
        return result