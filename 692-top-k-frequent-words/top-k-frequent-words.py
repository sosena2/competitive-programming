class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, (-freq, word)) 

        # Extract top k elements
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res