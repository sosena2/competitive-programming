class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        frequencies = [0]*k
        for x in arr:
            frequencies[x%k] += 1
        if k%2 == 0 and frequencies[k//2]%2 == 1:
            return False
        for i in range(1, k):
            if frequencies[i] != frequencies[(-i)%k]:
                return False
        return True
           

        