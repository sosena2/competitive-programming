class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        visited = set()

        def dfs(r, c):
            visited.add((r, c))
            for rw, cl in directions:
                nw_r = r + rw
                nw_cl = c + cl
                if inbound(nw_r, nw_cl) and grid[nw_r][nw_cl] == '1' and  (nw_r, nw_cl) not in visited:
                    dfs(nw_r, nw_cl)

        count = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    count += 1
        return count

