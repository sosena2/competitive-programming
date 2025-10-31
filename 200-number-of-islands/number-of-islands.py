class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        visited = set()
        queue = deque()
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    queue.append((i, j))
                    visited.add((i, j))
                    count += 1

                while queue:
                    rw, cl = queue.popleft()
                    for row, col in directions:
                        new_rw = row + rw
                        new_cl = col + cl
                        if inbound(new_rw, new_cl) and (new_rw, new_cl) not in visited and grid[new_rw][new_cl] == '1':

                            visited.add((new_rw, new_cl))
                            queue.append((new_rw, new_cl))

        return count

                



            