class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [num for num in nums]   
        
        for i in range(n-1): 
            for j in range(len(dp)-1):
                dp[j] = (dp[j] + dp[j+1]) % 10
            dp.pop() 

        return dp[0] 
