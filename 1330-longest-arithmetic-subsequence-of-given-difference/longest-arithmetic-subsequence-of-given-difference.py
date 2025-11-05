class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_length = 0
        
        for x in arr:
            prev = x - difference
            dp[x] = dp.get(prev, 0) + 1
            max_length = max(max_length, dp[x])
        
        return max_length