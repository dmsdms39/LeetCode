class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for i in range(numRows)]
        forward = True
        depth = 0

        for char in s:
            if depth == numRows - 1 and forward:
                forward = False

            elif depth == 0 and not forward:
                forward = True

            dir = 0 if numRows == 1 else (1 if forward else -1)
            
            rows[depth].append(char)
            depth += dir

        return ''.join([''.join(row) for row in rows])