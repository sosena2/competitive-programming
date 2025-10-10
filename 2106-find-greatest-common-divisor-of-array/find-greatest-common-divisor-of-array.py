class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        gcd = 0
        for num in range(1, min_num + 1):
            if min_num % num == 0 and max_num % num == 0:
                gcd = max(gcd, num)
        return gcd

