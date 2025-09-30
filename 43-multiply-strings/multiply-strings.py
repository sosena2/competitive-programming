class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        res = [0] * (n + m)

        num1, num2 = num1[::-1], num2[::-1]

        for i in range(n):
            for j in range(m):
                digit_mul = int(num1[i]) * int(num2[j])
                res[i + j] += digit_mul
            
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return ''.join(map(str, res[::-1]))