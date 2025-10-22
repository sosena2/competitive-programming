class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))

        dist = [0] * n
        dist[start_node] = 1
        pq = [(-1, start_node)]  

        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob  

            if node == end_node:
                return prob

            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > dist[neighbor]:
                    dist[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))

        return 0