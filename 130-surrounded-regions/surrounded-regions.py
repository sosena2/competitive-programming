class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        # """
        n = len(board)
        m = len(board[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        def dfs(r, c):
            if not inbound(r, c) or board[r][c]!= 'O':
                return 
                
            board[r][c] = '#'

            for rw, cl in directions:
                new_r = rw + r
                new_c = cl + c
                if inbound(new_r, new_c) and board[new_r][new_c] == 'O':
                    dfs(new_r, new_c)

        # first start the dfs from the edges and mark the 'O' boards as #
        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m-1] == 'O':
                dfs(i, m-1)

        for j in range(m):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[n-1][j] == 'O':
                dfs(n-1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


        

            
            

        