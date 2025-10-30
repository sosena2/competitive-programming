class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def result_sum(arr, n):
            total = 0
            for num in nums:
                total += ceil(num / n)
            return total
        low = 1
        high = max(nums)

        ans = 0
        while low <= high:
            mid = (low + high) // 2
            res = result_sum(nums, mid)
            if res <= threshold:
                ans = mid
                high = mid -1
            else:
                low = mid + 1
        return ans

        