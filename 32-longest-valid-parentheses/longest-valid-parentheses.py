class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = []
        last_invalid = -1 

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        max_len = max(max_len, i - stack[-1])
                    else:
                        max_len = max(max_len, i - last_invalid)
                else:
                    last_invalid = i


        return max_len 