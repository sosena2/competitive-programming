class Solution:
    def mySqrt(self, x: int) -> int:
        # brute 
        if x == 0:
            return 0
        ans = 1
        for i in range(1, x+1):
            if i * i <= x:
                ans = i 
            else:
                break
        return ans
