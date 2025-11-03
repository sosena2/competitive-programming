class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])

        def inbound(r, c):
            return 0<= r < row and 0 <= c < col

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        dist = [[float('inf')] * col for _ in range(row)]

        queue = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    dist[i][j] = 0
        
        while queue:
            r, c = queue.popleft()

            for rw, cl in directions:
                nw_r = r + rw
                nw_c = c + cl

                if inbound(nw_r, nw_c) and dist[nw_r][nw_c] > dist[r][c] + 1:
                    dist[nw_r][nw_c] = dist[r][c] + 1
                    queue.append((nw_r, nw_c))

        return dist
