class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ('+', '-', '*', '/')
        stack = []
        for token in tokens:
            if token in operators:
                right_token = stack.pop()
                left_token = stack.pop()
                if token == '+':
                    stack.append(left_token + right_token)
                elif token == '-':
                    stack.append(left_token - right_token)
                elif token == '*':
                    stack.append(left_token * right_token)
                else:
                    print(left_token / right_token)
                    stack.append(int(left_token / right_token))
            else:
                stack.append(int(token))
        
        return stack[0]
