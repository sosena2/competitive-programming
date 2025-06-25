class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                val = stack.pop()
                diff = i - val
                ans[val] = diff
            stack.append(i)
        return ans