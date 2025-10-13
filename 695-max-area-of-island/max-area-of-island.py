class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col
        
        visited = set()
        max_val = 0

        def dfs(r, c):
            visited.add((r, c))
            count = 1
            for rw, cl in directions:
                new_r = r + rw
                new_c = c + cl
                if inbound(new_r, new_c) and (new_r, new_c) not in visited and grid[new_r][new_c]==1:
                    count+=dfs(new_r, new_c)
            return count
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count = dfs(i, j)
                    max_val = max(max_val, count)
        
        return max_val
