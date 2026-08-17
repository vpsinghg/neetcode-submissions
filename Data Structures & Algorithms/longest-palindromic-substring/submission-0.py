class Solution:

    def searchPalindrome(self, left, right, s):
        n = len(s)

        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        # We went one step too far on both sides
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 0:
            return ""

        start = end = 0

        for i in range(n):

            # Odd length
            l1, r1 = self.searchPalindrome(i, i, s)

            # Even length
            l2, r2 = self.searchPalindrome(i, i + 1, s)

            if r1 - l1 > end - start:
                start, end = l1, r1

            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]