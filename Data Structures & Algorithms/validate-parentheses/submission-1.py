class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        esleme = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif ch in ")}]":
                if not stack or stack[-1] != esleme[ch]:
                    return False
                stack.pop()
        return not stack

        