class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        visited = set()
        perimeter = 0
    
        def dfs(r, c):
            nonlocal perimeter
            visited.add((r, c))

            for rw, cl in directions:
                nw_r = r + rw
                nw_cl = c + cl

                if not inbound(nw_r, nw_cl):
                        perimeter += 1
                if inbound(nw_r, nw_cl) and (nw_r, nw_cl) not in visited:
                    if grid[nw_r][nw_cl] == 0:
                        perimeter += 1
                    if grid[nw_r][nw_cl] == 1:
                        dfs(nw_r, nw_cl)

        for row in range(n):
            for col in range(m):
                if (row, col) not in visited and grid[row][col] == 1:
                    dfs(row, col)
        return perimeter



        
        