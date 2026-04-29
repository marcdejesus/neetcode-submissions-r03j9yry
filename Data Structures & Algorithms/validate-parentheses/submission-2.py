class Solution:
    def isValid(self, s: str) -> bool:
        
        brackstack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                brackstack.append(c)
            else:
                if not brackstack:
                    return False
                val = brackstack.pop()
                if c == ')' and val != '(':
                    return False
                elif c == '}' and val != '{':
                    return False
                elif c == ']' and val != '[':
                    return False
        return not brackstack