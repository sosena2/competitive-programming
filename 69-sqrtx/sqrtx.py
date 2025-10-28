class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        ans = 0
        low = 0
        high = x - 1
        while low <= high:
            mid = (low + high) // 2
            val = mid + 1
            if val * val <= x:
                ans = val
                low = mid + 1
            else:
                high = mid - 1
        return ans

        
