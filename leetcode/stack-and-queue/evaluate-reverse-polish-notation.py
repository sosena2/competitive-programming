class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:   
            if char == "+":
               if len(stack) >= 2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    val3 = val1 + val2
                    stack.append(val3)
            elif char == "*":
                if len(stack) >= 2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    val3 = val1 * val2
                    stack.append(val3)
            elif char == "-":
                if len(stack) >= 2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    val3 = val2 - val1
                    stack.append(val3)
            elif char == "/":
                if len(stack) >= 2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    val3 = int(val2 / val1)
                    stack.append(val3)
            else:
                stack.append(int(char))
        return stack[-1]