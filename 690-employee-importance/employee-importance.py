"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        imp = {}
        graph = {}
        n = len(employees)
        visited = set()
        count = 0

        for i in range(n):
            id_n = employees[i].id
            imp[id_n] = (employees[i].importance)
            graph[id_n] = (employees[i].subordinates)
        
        def dfs(node):
            if not node:
                return 

            nonlocal count
            count += imp[node]
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
            return count
        return dfs(id)
    
    