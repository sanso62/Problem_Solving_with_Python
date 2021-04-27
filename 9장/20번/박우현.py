class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis=list()
        
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                parenthesis.append(s[i])
            else:
                if len(parenthesis)==0:
                    return False
                symbol=parenthesis.pop()
                if symbol=='(':
                    if s[i]!=')':
                        return False
                elif symbol=='{':
                    if s[i]!='}':
                        return False
                elif symbol=='[':
                    if s[i]!=']':
                        return False

        return len(parenthesis)==0
