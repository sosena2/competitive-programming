class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for a, b in edges:
            graph[a].append(b)
            indegree[b]+=1
        
        def helper(node):
            # if not node:
            #     return 
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    helper(neighbour)
                    # visited.add(neighbour)

        for i in range(n):
            visited = set()
            helper(i)
            if len(visited) == n:
                return i
        return -1
                
            



        
