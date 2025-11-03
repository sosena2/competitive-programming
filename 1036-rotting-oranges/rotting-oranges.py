class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def inbound(r, c):
           return 0 <= r < row and 0 <= c < col
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        queue = deque()
        visited = set()
        time = 0
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
            
                for rw, cl in directions:
                    new_rw =  r + rw
                    new_cl = c + cl

                    if inbound(new_rw, new_cl) and (new_rw, new_cl) not in visited and grid[new_rw][new_cl] == 1:
                        grid[new_rw][new_cl] = 2
                        fresh -= 1
                        queue.append((new_rw, new_cl))
                        visited.add((new_rw, new_cl))
                        
            # time should be incremented for every level in bfs
            time += 1

        if fresh == 0:
            return time
        else:
            return -1

        

       





        