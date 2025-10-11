class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        

        DIRS = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }
        
        conn = {
            1: ['L', 'R'],
            2: ['U', 'D'],
            3: ['L', 'D'],
            4: ['R', 'D'],
            5: ['L', 'U'],
            6: ['R', 'U'],
        }
    
        opp = {
            'L': 'R', 'R': 'L',
            'U': 'D', 'D': 'U'
        }
        
        visited = [[False]*n for _ in range(m)]
        
        def dfs(i, j) -> bool:
            if i == m-1 and j == n-1:
                return True
            visited[i][j] = True
            
            cur_type = grid[i][j]
            for d in conn[cur_type]:
                di, dj = DIRS[d]
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    # Check if neighbor’s street type allows coming from the opposite direction
                    neigh_type = grid[ni][nj]
                    if opp[d] in conn[neigh_type]:
                        if dfs(ni, nj):
                            return True
            
            return False
        
        return dfs(0, 0)