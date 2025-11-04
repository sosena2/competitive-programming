class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        or_all = 0
        for num in nums:
            or_all |= num
        subsets = pow(2, n-1)
        return subsets * or_all
