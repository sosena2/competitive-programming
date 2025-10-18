class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        curr = []
        for ch in s:
            if ch == '(':
                st.append(''.join(curr))
                curr = []
            elif ch == ')':
                curr.reverse()
                prev = st.pop()
                curr = list(prev) + curr
            else:
                curr.append(ch)
        return ''.join(curr) 