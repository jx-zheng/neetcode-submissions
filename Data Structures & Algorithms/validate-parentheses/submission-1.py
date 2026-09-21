class Solution:
    def isValid(self, s: str) -> bool:
        parens_map = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []
        for char in s:
            if char in parens_map:
                if not stack:
                    return False
                if stack[-1] != parens_map[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
            
        return not stack
