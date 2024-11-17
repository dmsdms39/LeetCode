class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for i in range(numRows)]
        forward = True
            
        def recursive(idx, depth, forward):
            if idx == len(s):
                return
            
            if depth == numRows - 1 and forward:
                forward = False

            elif depth == 0 and not forward:
                forward = True

            dir = 0 if numRows == 1 else (1 if forward else -1)
            
            rows[depth].append(s[idx])
            recursive(idx + 1, depth + dir, forward)
        
        recursive(0, 0, forward)      

        return ''.join([''.join(row) for row in rows])