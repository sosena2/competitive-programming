class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def dp(idx):
            if idx > len(questions) - 1:
                return 0

            points, brainpower = questions[idx]

            if idx in memo:
                return memo[idx]

            # take 
            take = dp(idx + brainpower +1) + points
            # not_take
            not_take = dp(idx + 1)
            memo[idx] = max(not_take, take)
            return memo[idx]
        return dp(0)

        