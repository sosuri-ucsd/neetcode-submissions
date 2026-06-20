class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        frame = {'[': ']', '{': '}', '(': ')'}
        for i in s:
            if i in frame:
                stack.append(i)
            else:
                if not stack or frame[stack[-1]] != i:
                    return False
                stack.pop()
        return stack == []
            