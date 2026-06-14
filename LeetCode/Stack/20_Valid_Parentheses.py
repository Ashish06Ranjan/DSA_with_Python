"""

Problem : 20 Valid Parentheses

Approach : When you see an opening bracket, put it in a stack.
           When you see a closing bracket, check whether it matches the latest opening bracket.
           If not, return False. At the end, the stack must be empty.
           
"""

class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()

        return len(stack) == 0
