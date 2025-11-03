class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = []

        def dfs(node):
            path.append(node)
            if node == len(graph) - 1:
                res.append(path.copy())
            else:
                for nei in graph[node]:
                    dfs(nei)
            path.pop()

        dfs(0)
        return res

