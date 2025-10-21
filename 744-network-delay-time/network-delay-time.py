class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))

        distances = [float('inf') for _ in range(n+1)]
        distances[k] = 0

        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            dist, node = heapq.heappop(pq)
    
            for v, w in adj_list[node]:
                if dist + w < distances[v]:
                    distances[v] = dist + w
                    heapq.heappush(pq, (dist + w, v))
        ans = max(distances[1:])
        return -1 if ans == float('inf') else ans
