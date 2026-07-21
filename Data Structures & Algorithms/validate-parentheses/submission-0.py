class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {'}' : '{',
                    ')' : '(',
                    ']' : '['
                }

        for paren in s:

            if paren in '{[(':

                stack.append(paren)

            else:

                if not stack:

                    return False

                if stack[-1] == pairs[paren]:

                    stack.pop()
                else:
                    return False
        return not stack
        