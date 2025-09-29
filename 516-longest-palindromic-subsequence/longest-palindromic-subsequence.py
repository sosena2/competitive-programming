class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # top down
        memo = [[-1]*len(s) for _ in range(len(s))]
        def dp(i, j):
            # base case
            if i > j:
                return 0
            if i == j:
                return 1
            if memo[i][j]!=-1:
                return memo[i][j]
            # take not take
            take = 0
            not_take = max( dp(i, j - 1) , dp(i + 1, j ))
            if s[i] == s[j]:
                take = dp(i+1, j-1) + 2    
            memo[i][j] =  max(take , not_take)
            return memo[i][j]
        return dp(0, len(s)-1)
            

    