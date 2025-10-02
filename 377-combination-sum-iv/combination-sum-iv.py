class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # top down
        n = len(nums)
        memo = {}
        def dp(t):
            
            if t == 0:
                return 1
            
            if (t) in memo:
                return memo[t]
            
            way = 0
            for num in nums:
                if t - num >= 0:
                    way += dp(t - num)
            
            memo[t] = way
            return memo[t]
        return dp(target)
