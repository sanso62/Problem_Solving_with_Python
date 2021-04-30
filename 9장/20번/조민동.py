class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["[", "{", "("]:
                stack.append(c)
            else:
                if stack == []:
                    return False
                elif stack[-1] == "[" and c == "]":
                    stack.pop()
                elif stack[-1] == "{" and c == "}":
                    stack.pop()
                elif stack[-1] == "(" and c == ")":
                    stack.pop()
                else:
                    break


        if stack==[]:
            return True
        else:
            return False
