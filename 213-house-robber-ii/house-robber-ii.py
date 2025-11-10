class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(houses):
            prev1 = prev2 = 0
            for num in houses:
                prev1, prev2 = max(prev1, prev2 + num), prev1
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
