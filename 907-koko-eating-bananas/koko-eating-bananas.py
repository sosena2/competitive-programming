class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # optimized binary search solution
        def required(arr, hr):
            total = 0
            for i in range(len(piles)):
                total += ceil(arr[i]/hr)
            return total
        high = max(piles)
        low = 1
        ans = 0
        while low <= high:
            mid = (high + low) // 2
            time = required(piles, mid)
            if time <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

        

            
