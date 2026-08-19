class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        l = 0
        r = n-1
        while(l<r):
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if ord(s[l].lower()) != ord(s[r].lower()):
                    return False
                
                l += 1
                r -= 1
        return True
        