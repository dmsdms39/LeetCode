class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirIdx = 0
        output = []

        while matrix:
            if len(matrix[0]) < 1:
                break
            elif dirIdx == 0:
                output.extend(matrix.pop(0))
                dirIdx = 1
            elif dirIdx == 1:
                for lst in matrix:
                    output.append(lst.pop(-1))
                dirIdx = 2
            elif dirIdx == 2:
                output.extend(matrix.pop(-1)[::-1])
                dirIdx = 3
            elif dirIdx == 3:
                for lst in matrix[::-1]:
                    output.append(lst.pop(0))
                dirIdx = 0
        return output

            