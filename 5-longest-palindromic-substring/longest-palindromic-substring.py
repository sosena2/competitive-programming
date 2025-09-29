class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        
        def expandAroundCenter(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1  
        
        for i in range(len(s)):
            # Odd length 
            l1, r1 = expandAroundCenter(i, i)
            # Even length 
            l2, r2 = expandAroundCenter(i, i + 1)
            
            # Update longest if needed
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        
        return s[start:end + 1]
