class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(arr, n):
            day = 1
            total = 0
            for w in weights:
                total += w
                if total > n:
                    day += 1
                    total = w
            return day
        
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2
            d = helper(weights, mid)
            if d <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        


        