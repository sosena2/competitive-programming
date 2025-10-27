class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = float('inf')
        for i in range(len(nums)):
            if nums[i] < min_val:
                min_val = nums[i]
        return min_val
