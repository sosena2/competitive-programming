class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def bouquets(arr, day):
            count = 0
            b = 0
            for num in bloomDay:
                if num <= day:
                    count += 1
                else:
                    count = 0
                if count == k:
                    b += 1
                    count = 0
            return b
        
        minm = m*k
        ans = 0
        if len(bloomDay) < minm:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:
            mid = (low + high)//2
            bq = bouquets(bloomDay, mid)
            if bq >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return  ans if ans!= 0 else -1
            
        
