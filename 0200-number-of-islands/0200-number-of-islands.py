class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        rows, columns = len(grid), len(grid[0])
        
        def bfs(x, y):
            dd = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            q = [(x,y)]
            grid[x][y] = "0"

            while q:
                cx, cy = q.pop()
                for (dx, dy) in dd:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < rows and 0 <= ny < columns and grid[nx][ny] == "1":
                        q.append((nx, ny))
                        grid[nx][ny] = "0"


        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    bfs(r, c)
                    island += 1

                        
        return island