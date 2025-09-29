class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # top down
        # memo = [[-1]*len(s) for _ in range(len(s))]
        # def dp(i, j):
        #     # base case
        #     if i > j:
        #         return 0
        #     if i == j:
        #         return 1
        #     if memo[i][j]!=-1:
        #         return memo[i][j]
        #     # take not take
        #     take = 0
        #     not_take = max( dp(i, j - 1) , dp(i + 1, j ))
        #     if s[i] == s[j]:
        #         take = dp(i+1, j-1) + 2    
        #     memo[i][j] =  max(take , not_take)
        #     return memo[i][j]
        # return dp(0, len(s)-1)

        # buttom up
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            # initialize by filling the diagonal
            dp[i][i] = 1
        for d in range(1, len(s)):
            for l in range(len(s)-d):
                r = l + d
            
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1] + 2  
                else:
                    dp[l][r] = max( dp[l][r - 1] , dp[l + 1][ r ])
        return dp[0][len(s)-1]




            

    