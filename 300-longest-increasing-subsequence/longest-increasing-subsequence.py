class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #buttom up
        n = len(nums)
        # all numbers are subsequences of length 1 by themselves
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
       



            
       

            
    


