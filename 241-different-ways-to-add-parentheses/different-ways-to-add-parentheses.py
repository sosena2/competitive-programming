class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}

        def ways(expr):
            if expr in memo:
                return memo[expr]
            
            res = []
            for i, ch in enumerate(expr):
                if ch in '+-*':
                    left = ways(expr[:i])
                    right = ways(expr[i+1:])
                    
                    for a in left:
                        for b in right:
                            if ch == '+':
                                res.append(a + b)
                            elif ch == '-':
                                res.append(a - b)
                            else:
                                res.append(a * b)
            
            if not res:  
                res = [int(expr)]
            
            memo[expr] = res
            return res

        return ways(expression)
