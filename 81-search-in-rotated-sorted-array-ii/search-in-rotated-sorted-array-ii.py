
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
        
            if nums[mid] == target:
                return True
            
            else:
                 # we will shrink the search space
                if nums[low] == nums[mid] == nums[high]:
                    low += 1
                    high -= 1
                    continue
                # if the left half is sorted and target is found in sorted
                if nums[low] <= nums[mid]:
                    if nums[low] <= target and target <= nums[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    if nums[mid] <= nums[high]:
                        if nums[mid] <= target and target <= nums[high]:
                            low = mid + 1
                        else:
                            high = mid - 1
                    
        return False