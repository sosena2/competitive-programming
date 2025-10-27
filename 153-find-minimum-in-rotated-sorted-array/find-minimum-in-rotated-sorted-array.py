class Solution:
    def findMin(self, nums: List[int]) -> int:
        # optimized solution using binary search
        # approach pich the smallest from the sorted right or left half and eliminate
        low = 0
        high = len(nums)- 1
        min_val = float('inf')
        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:
                min_val = min(nums[low], min_val)
                low = mid + 1
            elif nums[mid] <= nums[high]:
                min_val = min(nums[mid], min_val)
                high = mid - 1
        return min_val