from collections import Deque

def isPalindrome(self, s:str) :
    
    strs : Deque = collections.deque()
    
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
            
    while len(strs) > 1 :
         if strs.pop(0) != strs.pop():
            return False
    return True
