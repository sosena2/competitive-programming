class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        def helper(i):
            # we can get to the position 1 and 0 for free
            if i < 2:
                return 0

            if i in memo:
                return memo[i]

            one_step = helper(i-1) + cost[i-1]
            two_step = helper(i-2) + cost[i-2]
            memo[i] = min(one_step, two_step)
            return memo[i]
        return helper(n)
        

        

        