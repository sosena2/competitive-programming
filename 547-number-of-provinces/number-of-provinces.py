class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    if i != j:
                        graph[i].append(j)
        
        visited = set()
        count = 0
     
        def dfs(node):
    
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
            
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count


        

        
        