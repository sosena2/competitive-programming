class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # bfs
        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    if i != j:
                        graph[i].append(j)
            
        visited = set()
        provinces = 0
        

        for i in range(n):
            if i not in visited:
                visited.add(i)
                provinces += 1
                queue = deque([i])

                while queue:
                    node = queue.popleft()
                    for neighbour in graph[node]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
        return provinces
                
        