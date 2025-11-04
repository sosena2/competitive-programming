class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p

        if rem == 0:
            return 0
        
        prefix_sum = 0
        min_len = float('inf')
        store = {0: -1}  
        
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            target = (prefix_sum - rem) % p  
            
            if target in store:
                min_len = min(min_len, i - store[target])
            
            store[prefix_sum] = i  
        
        return min_len if min_len < len(nums) else -1
