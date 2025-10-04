class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # top dowm
        memo = {}
        def helper(i, j):
            if i >= len(text1) and j >= len(text2):
                return 0
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            take = 0
            if text1[i] == text2[j]:
                take = helper(i + 1, j + 1) + 1
            else:
                not_take = max(helper(i + 1, j), helper(i, j+1))
            memo[(i, j)] = take or not_take
            return memo[(i, j)]
        return helper(0, 0)

        
        
      
       