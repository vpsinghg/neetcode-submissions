class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_freq = 0
        ans = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Maximum frequency seen in the current/previous windows
            max_freq = max(max_freq, freq[s[right]])

            # Shrink window until it becomes valid
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans 