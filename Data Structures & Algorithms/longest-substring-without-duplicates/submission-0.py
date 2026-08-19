from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        left = 0
        right = 0
        hash_map = defaultdict(int)
        longest = 0

        while right < n:
            hash_map[s[right]] += 1

            if len(hash_map) == (right - left + 1):
                # valid
                longest = max(longest, right - left + 1)
            else:
                while len(hash_map) != (right - left + 1):
                    hash_map[s[left]] -= 1
                    if hash_map[s[left]] == 0:
                        del hash_map[s[left]]

                    left += 1

            right += 1

        return longest
