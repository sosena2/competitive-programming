class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_positions = {stone: i for i, stone in enumerate(stones)}
        memo = {}

        def dp(idx, jump):
            
            if idx == len(stones) - 1:
                return True

            if (idx, jump) in memo:
                return memo[(idx, jump)]

            current_pos = stones[idx]
            for step in [jump - 1, jump, jump + 1]:
                if step > 0:
                    next_pos = current_pos + step
                    if next_pos in stone_positions:
                        next_idx = stone_positions[next_pos]
                        if dp(next_idx, step):
                            memo[(idx, jump)] = True
                            return True

            memo[(idx, jump)] = False
            return False

        if stones[1] != 1:
            return False

        return dp(1, 1)
