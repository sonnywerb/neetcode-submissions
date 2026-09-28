class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        pairs = {')' :'(',
                 '}': "{",
                 ']': '['
                }
        
        stack = []
        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if len(stack) == 0 or pairs[c] != stack.pop():
                    return False
        
        return False if stack else True