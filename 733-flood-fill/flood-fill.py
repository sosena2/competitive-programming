class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])

        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col

        original = image[sr][sc]

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = deque([(sr, sc)])
        visited = set([(sr, sc)])
        
        while queue:
            r, c = queue.popleft()
            image[r][c] = color

            for rw, cl in directions:
                new_rw = r + rw
                new_cl = c + cl
                if inbound(new_rw, new_cl) and (new_rw, new_cl) not in visited and image[new_rw][new_cl] == original:
                    queue.append([new_rw, new_cl])
                    visited.add((new_rw, new_cl))
        return image

        
        
