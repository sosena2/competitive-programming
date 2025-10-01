class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        # taking the first and last index as a state
        def dp(i, j, turn):
            if i > j:
                return 0

            if (i, j, turn) in memo:
                return memo[(i, j, turn)]

            if turn == 1:
                ans = max(dp(i+1, j, 0) + piles[i], dp(i, j - 1, 0) + piles[j]) 
            else:
                ans = max(dp(i+1, j, 1) + piles[i], dp(i, j - 1, 1) + piles[j])
                
            memo[(i, j, turn)] = ans
            return ans
        alice = dp(0, len(piles)-1, 1)
        total = sum(piles)
        bob = total - alice
        return alice > bob


            


         
            

