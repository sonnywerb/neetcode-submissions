class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {')':'(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c in p_map:
                if stack and stack[-1] == p_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
                