class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        
        arr = [(s, i) for i, s in enumerate(score)]
        arr.sort(reverse=True)
        res = [""] * n
        
        for rank, (s, i) in enumerate(arr):
            if rank == 0:
                res[i] = "Gold Medal"
            elif rank == 1:
                res[i] = "Silver Medal"
            elif rank == 2:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(rank + 1)
        
        return res