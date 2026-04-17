class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # lower bound
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                high = mid -1
            else:
                low = mid + 1
        lower = low
        
        # upper bound
        low2 = 0
        high2 = len(nums) - 1

        while low2 <= high2:
            mid = (low2 + high2) // 2

            if nums[mid] > target:
                high2 = mid -1
            else:
                low2 = mid + 1
            
        higher = low2

        if lower == len(nums) or nums[lower] != target:
            return [-1, -1]

        return [lower, higher - 1]
