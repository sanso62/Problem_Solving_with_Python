class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []
        table = {')':'(',']':'[','}':'{'}
        
        for c in s:
            if c not in table: #stack에 append
                stack.append(c)
            elif not stack or table[c]!=stack.pop(): #stack.pop 제거!
                return False
        return len(stack) == 0 #True 반환
