class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        if n <= 2:
            return 0
            
        is_prime = [True] * (n)
        
        # 1 and 2 are neither prime nor composite
        is_prime[0] = is_prime[1] = False
        i = 2
        while i < n:
            if is_prime[i]:
                j = 2 * i
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1
        
        for val in is_prime:
            if val == True:
                count += 1

        return count


        


        