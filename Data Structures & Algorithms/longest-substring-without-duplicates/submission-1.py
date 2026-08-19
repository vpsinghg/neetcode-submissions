from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        longest = 0
        freq = defaultdict(int)

        for right in range(len(s)):
            freq[s[right]] += 1

            while len(freq) != right - left + 1:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            longest = max(longest, right - left + 1)

        return longest