import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove character except digit, alphabet
        s=s.lower()
        s = re.sub('[\W_]', "", s)
        print(s)
        # check reverse
        print(s[::-1])
        if s == s[::-1]:
            return True
        else:
            return False
