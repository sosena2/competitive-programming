class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        counts = [0] * 10
        cows = 0

        for s_ch, g_ch in zip(secret, guess):
            if s_ch == g_ch:
                bulls += 1
            else:
                s = ord(s_ch) - ord('0')
                g = ord(g_ch) - ord('0')

                if counts[s] < 0:
                    cows += 1
               
                if counts[g] > 0:
                    cows += 1
                    
                counts[s] += 1
                counts[g] -= 1

        return f"{bulls}A{cows}B"