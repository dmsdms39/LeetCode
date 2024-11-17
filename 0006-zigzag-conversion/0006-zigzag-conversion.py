class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * (numRows)
        
        if numRows == 1:
            return s

        forward = True
        depth = 0

        for char in s:
            if depth == numRows - 1 and forward:
                forward = False

            elif depth == 0 and not forward:
                forward = True

            dir = 1 if forward else -1
            
            rows[depth] += char
            depth += dir

        return ''.join(rows)