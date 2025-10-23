class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        positions = defaultdict(list)
        
        for i, ch in enumerate(ring):
            positions[ch].append(i)
        
        @lru_cache(None)
        def dfs(pos, i):

            if i == len(key):
                return 0
            
            res = float('inf')
            for j in positions[key[i]]:

                diff = abs(pos - j)
                step = min(diff, n - diff)
                res = min(res, step + 1 + dfs(j, i + 1)) 
            
            return res
        
        return dfs(0, 0)