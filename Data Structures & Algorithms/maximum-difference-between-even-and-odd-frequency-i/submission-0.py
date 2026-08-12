class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        odd = max(v for v in freq.values() if v % 2)
        even = min(v for v in freq.values() if v % 2 == 0)
        return odd - even