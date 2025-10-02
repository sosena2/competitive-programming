class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        n = len(word1)
        m = len(word2)

        if word1 == word2:
            return 0

        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))

        def dp(i, j):
            # base cases
            if i == n and j == m:
                return 0

            if i == n:
                return m - j

            if j == m:
                return n - i

            if (i, j) in memo:
                return memo[(i, j)]

            take = 0
            if word1[i] == word2[j]:
                take = dp(i+1, j +1) 
                memo[(i, j)] = take
            else:
                rem = dp(i+1, j)
                rep = dp(i+1, j+1)
                ins = dp(i, j+1)
                memo[(i, j)] = min(rem, rep, ins) + 1
            return memo[(i, j)]
        return dp(0, 0)
            
